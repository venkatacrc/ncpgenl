'use strict';

// Phone/web version of GenL Cards. Cards are drawn by the shared cardkit renderer
// (GLCard in cardkit/card.js), the same one the Mac app uses.

const $ = (sel) => document.querySelector(sel);

function h(tag, attrs = {}, ...children) {
    const el = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
        if (v == null || v === false) continue;
        if (k === 'class') el.className = v;
        else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
        else if (typeof v === 'boolean') el[k] = v;
        else el.setAttribute(k, v);
    }
    for (const c of children.flat()) {
        if (c == null || c === false) continue;
        el.append(c instanceof Node ? c : String(c));
    }
    return el;
}

// ---- Saved state (localStorage) ----

const saved = {
    get(key, fallback) {
        try {
            const v = localStorage.getItem('genlCards.' + key);
            return v == null ? fallback : JSON.parse(v);
        } catch {
            return fallback;
        }
    },
    set(key, value) {
        localStorage.setItem('genlCards.' + key, JSON.stringify(value));
    },
};

const KINDS = [
    ['all', 'All'], ['lesson', 'Lessons'], ['concept', 'Concepts'], ['verse', 'Verses'],
    ['question', 'Questions'], ['trap', 'Traps'], ['reading', 'Readings'],
];
const NOUNS = {
    all: 'cards', lesson: 'lesson cards', concept: 'concept cards', verse: 'verses',
    question: 'questions', trap: 'traps', reading: 'readings',
};
const PRACTICE = [['all', 'All cards'], ['notKnown', 'Not yet known'], ['review', 'Review only'], ['due', 'Due today']];

const prefs = {
    selected: saved.get('selected', '*'),
    kind: saved.get('kind', 'lesson'),
    study: saved.get('study', 'learn'),
    practice: saved.get('practice', 'all'),
    shuffle: saved.get('shuffle', false),
    collapsed: saved.get('collapsed', []),
    print: saved.get('print', { answers: true, notes: true, reviewOnly: false }),
};

function setPref(key, value) {
    prefs[key] = value;
    saved.set(key, value);
}

/** Known/review marks plus a five-box Leitner schedule driven by Test mode answers. */
const INTERVALS = { 1: 1, 2: 3, 3: 7, 4: 14, 5: 30 };
const progress = {
    known: new Set(saved.get('known', [])),
    review: new Set(saved.get('review', [])),
    box: saved.get('box', {}),
    due: saved.get('due', {}),
    save() {
        saved.set('known', [...this.known]);
        saved.set('review', [...this.review]);
        saved.set('box', this.box);
        saved.set('due', this.due);
    },
    isDue(id) { return id in this.due && this.due[id] <= Date.now(); },
    toggleKnown(id) {
        if (this.known.delete(id)) return this.save();
        this.known.add(id); this.review.delete(id); this.save();
    },
    toggleReview(id) {
        if (this.review.delete(id)) return this.save();
        this.review.add(id); this.known.delete(id); this.save();
    },
    record(id, correct) {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        if (correct) {
            const next = Math.min((this.box[id] || 0) + 1, 5);
            this.box[id] = next;
            this.due[id] = today.getTime() + INTERVALS[next] * 86400000;
            this.known.add(id); this.review.delete(id);
        } else {
            this.box[id] = 1;
            this.due[id] = today.getTime();
            this.review.add(id); this.known.delete(id);
        }
        this.save();
    },
    reset() {
        this.known.clear(); this.review.clear(); this.box = {}; this.due = {}; this.save();
    },
};

const notes = {
    all: saved.get('notes', {}),
    set(id, text) {
        const t = text.trim();
        if (t) this.all[id] = t; else delete this.all[id];
        saved.set('notes', this.all);
    },
};

let deck = null;
let loadError = null;

const session = { order: [], position: 0, flipped: false, chosen: {}, answers: {}, finished: false };

// ---- Deck helpers ----

const groupKey = (src, group) => `${src}|${group}`;
const isQuestion = (c) => c.kind === 'question' && c.options && c.answer;
const matchesKind = (c) => prefs.kind === 'all' || c.kind === prefs.kind;

function allGroupKeys() {
    return deck.sources.flatMap((s) => s.groups.map((g) => groupKey(s.id, g.id)));
}

function selectedSet() {
    return new Set(prefs.selected === '*' ? allGroupKeys() : prefs.selected);
}

function setSelected(set) {
    const all = allGroupKeys();
    setPref('selected', all.every((k) => set.has(k)) ? '*' : [...set].sort());
}

function currentCard() {
    const i = session.order[session.position];
    return i != null && deck.cards[i] ? deck.cards[i] : null;
}

function selectedCards() {
    const sel = selectedSet();
    return deck.cards.filter((c) => matchesKind(c) && sel.has(groupKey(c.src, c.group)));
}

function revealed(card) {
    if (isQuestion(card)) return session.flipped || card.id in session.chosen;
    return prefs.study === 'learn' || session.flipped;
}

function shuffled(list) {
    const a = [...list];
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}

// ---- Session ----

function rebuild() {
    const sel = selectedSet();
    let picked = [];
    deck.cards.forEach((c, i) => { if (matchesKind(c) && sel.has(groupKey(c.src, c.group))) picked.push(i); });
    const id = (i) => deck.cards[i].id;
    if (prefs.practice === 'notKnown') picked = picked.filter((i) => !progress.known.has(id(i)));
    if (prefs.practice === 'review') picked = picked.filter((i) => progress.review.has(id(i)));
    if (prefs.practice === 'due') picked = picked.filter((i) => progress.isDue(id(i)));
    startSession(prefs.shuffle ? shuffled(picked) : picked);
}

function startSession(order) {
    Object.assign(session, { order, position: 0, flipped: false, chosen: {}, answers: {}, finished: false });
    render();
}

function move(delta) {
    const n = session.order.length;
    if (!n) return;
    session.position = (session.position + delta + n) % n;
    session.flipped = false;
    render();
}

function reveal() {
    const card = currentCard();
    if (!card || revealed(card)) return;
    session.flipped = true;
    render();
}

function choose(key) {
    const card = currentCard();
    if (!card || !isQuestion(card) || revealed(card)) return;
    session.chosen[card.id] = key;
    if (prefs.study === 'test') {
        const correct = key === card.answer;
        session.answers[card.id] = correct;
        progress.record(card.id, correct);
    }
    render();
}

function grade(correct) {
    const card = currentCard();
    if (!card || !session.flipped || isQuestion(card)) return;
    session.answers[card.id] = correct;
    progress.record(card.id, correct);
    advance();
}

function advance() {
    const n = session.order.length;
    for (let step = 1; step <= n; step++) {
        const p = (session.position + step) % n;
        if (!(deck.cards[session.order[p]].id in session.answers)) {
            session.position = p;
            session.flipped = false;
            render();
            return;
        }
    }
    session.finished = true;
    render();
}

// ---- Rendering ----

function render() {
    renderSwitches();
    renderStatus();
    renderStage();
    renderActions();
    if ($('#drawer').classList.contains('open')) renderDrawer();
}

function renderSwitches() {
    const chips = $('#kind-switch');
    if (!chips.children.length) {
        for (const [value, label] of KINDS) chips.append(h('button', { 'data-value': value }, label));
    }
    for (const b of chips.querySelectorAll('button')) b.classList.toggle('on', b.dataset.value === prefs.kind);
    for (const b of $('#study-switch').querySelectorAll('button')) b.classList.toggle('on', b.dataset.value === prefs.study);
}

function renderStatus() {
    const el = $('#status');
    el.replaceChildren();
    if (!deck || !session.order.length || (prefs.study === 'test' && session.finished)) return;
    const n = session.order.length;
    el.append(h('span', {}, h('strong', {}, `Card ${session.position + 1}`), ` of ${n}`));
    if (prefs.study === 'test') {
        const answered = Object.keys(session.answers).length;
        const correct = Object.values(session.answers).filter(Boolean).length;
        el.append(h('span', {}, `Score ${correct} of ${answered} · ${n - answered} to go`));
    } else {
        let known = 0, review = 0, due = 0;
        for (const i of session.order) {
            const id = deck.cards[i].id;
            if (progress.known.has(id)) known++;
            if (progress.review.has(id)) review++;
            if (progress.isDue(id)) due++;
        }
        el.append(h('span', {}, `Known ${known} · Review ${review} · Due ${due}`));
    }
}

function renderStage() {
    const stage = $('#stage');
    stage.replaceChildren();
    if (loadError) {
        stage.append(h('div', { class: 'empty' }, h('h2', {}, 'Could not load the cards'), h('p', {}, loadError)));
        return;
    }
    if (!deck) {
        stage.append(h('div', { class: 'empty' }, 'Loading cards…'));
        return;
    }
    if (prefs.study === 'test' && session.finished) {
        stage.append(testSummary());
        return;
    }
    const card = currentCard();
    if (!card) {
        stage.append(h('div', { class: 'empty' },
            h('div', { class: 'big' }, '🗂'),
            h('h2', {}, 'No cards to study'),
            h('p', {}, emptyHint()),
            h('button', { class: 'btn primary', onclick: openDrawer }, 'Choose groups')));
        return;
    }
    const open = revealed(card);
    const scroller = h('div', { class: 'card-scroll' });
    stage.append(scroller);
    GLCard.render(scroller, card, {
        flipped: open,
        known: progress.known.has(card.id),
        review: progress.review.has(card.id),
        box: progress.box[card.id],
        note: notes.all[card.id],
        chosen: session.chosen[card.id],
        hint: open ? null : isQuestion(card) ? 'Tap an answer.' : 'Recall it, then tap the card to reveal.',
    });
    addSwipe(scroller);
}

function emptyHint() {
    if (prefs.practice === 'review') return 'No cards are marked for review here.';
    if (prefs.practice === 'notKnown') return 'Every card in this selection is marked known.';
    if (prefs.practice === 'due') return 'Nothing is due today. Cards join the schedule when you answer them in Test mode.';
    return 'Tick at least one group, or pick another card type.';
}

function testSummary() {
    const correct = Object.values(session.answers).filter(Boolean).length;
    const missed = session.order.filter((i) => session.answers[deck.cards[i].id] === false);
    const total = session.order.length;
    const percent = total ? Math.round((correct / total) * 100) : 0;
    return h('div', { class: 'summary' },
        h('div', { class: 'big' }, missed.length ? '✅' : '⭐'),
        h('h2', {}, 'Test complete'),
        h('div', { class: 'score' }, `${correct} of ${total} correct (${percent}%)`),
        h('p', {}, missed.length
            ? `Correct cards moved up a box; the ${missed.length} you missed are due again today.`
            : 'Every card moved up a box in the review schedule.'),
        h('div', { class: 'buttons' },
            missed.length > 0 && h('button', {
                class: 'btn primary',
                onclick: () => startSession(prefs.shuffle ? shuffled(missed) : missed),
            }, `Retest the ${missed.length} missed`),
            h('button', { class: 'btn', onclick: rebuild }, 'Start a new test'),
            h('button', { class: 'btn', onclick: () => { setPref('study', 'learn'); rebuild(); } }, 'Switch to Learn')));
}

function renderActions() {
    const bar = $('#actions');
    bar.replaceChildren();
    const card = deck ? currentCard() : null;
    if (!card || (prefs.study === 'test' && session.finished)) return;
    const open = revealed(card);
    const prev = h('button', { class: 'btn small', onclick: () => move(-1), 'aria-label': 'Previous card' }, '‹');
    const next = h('button', { class: 'btn small', onclick: () => move(1), 'aria-label': 'Next card' }, '›');
    const note = h('button', { class: 'btn small', onclick: () => openNote(card), 'aria-label': 'Note' },
        notes.all[card.id] ? '📝' : '✎');
    const test = prefs.study === 'test';
    if (isQuestion(card) && !open) {
        bar.append(prev, h('button', { class: 'btn', onclick: () => { session.flipped = true; render(); } }, 'Show answer'), note, next);
    } else if (isQuestion(card) && test) {
        bar.append(prev, h('button', { class: 'btn primary', onclick: advance }, 'Next question'), note);
    } else if (test && !open) {
        bar.append(prev, h('button', { class: 'btn primary', onclick: reveal }, 'Show answer'),
            h('button', { class: 'btn small', onclick: () => move(1) }, 'Skip ›'));
    } else if (test) {
        bar.append(prev,
            h('button', { class: 'btn bad', onclick: () => grade(false) }, '✗ Missed it'),
            h('button', { class: 'btn good', onclick: () => grade(true) }, '✓ Got it'), note);
    } else {
        bar.append(prev,
            h('button', {
                class: 'btn' + (progress.known.has(card.id) ? ' on-known' : ''),
                onclick: () => { progress.toggleKnown(card.id); render(); },
            }, progress.known.has(card.id) ? '✓ Known' : 'Known'),
            h('button', {
                class: 'btn' + (progress.review.has(card.id) ? ' on-review' : ''),
                onclick: () => { progress.toggleReview(card.id); render(); },
            }, progress.review.has(card.id) ? '⚑ Review' : 'Review'),
            note, next);
    }
}

function addSwipe(el) {
    let x0 = null, y0 = null;
    el.addEventListener('touchstart', (e) => {
        x0 = e.touches[0].clientX;
        y0 = e.touches[0].clientY;
    }, { passive: true });
    el.addEventListener('touchend', (e) => {
        if (x0 == null) return;
        const dx = e.changedTouches[0].clientX - x0;
        const dy = e.changedTouches[0].clientY - y0;
        x0 = null;
        if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) move(dx < 0 ? 1 : -1);
    });
}

GLCard.onEvent = (type, data) => {
    if (type === 'flip') reveal();
    else if (type === 'choose') choose(data);
    else if (type === 'link') window.open(data, '_blank', 'noopener');
};

// ---- Drawer: groups and options ----

function openDrawer() {
    renderDrawer();
    $('#drawer').classList.add('open');
    $('#drawer').setAttribute('aria-hidden', 'false');
    $('#backdrop').hidden = false;
}

function closeDrawer() {
    $('#drawer').classList.remove('open');
    $('#drawer').setAttribute('aria-hidden', 'true');
    $('#backdrop').hidden = true;
}

function checkRow(label, checked, onchange, count) {
    const id = 'c' + Math.random().toString(36).slice(2);
    return h('div', { class: 'row' },
        h('input', { type: 'checkbox', id, checked, onchange: (e) => onchange(e.target.checked) }),
        h('label', { for: id }, label),
        count != null && h('span', { class: 'n' }, String(count)));
}

function renderDrawer() {
    const body = $('#drawer-body');
    const scroll = body.scrollTop;
    body.replaceChildren();
    if (!deck) return;

    const practice = h('select', { onchange: (e) => { setPref('practice', e.target.value); rebuild(); } },
        PRACTICE.map(([v, t]) => h('option', { value: v, selected: prefs.practice === v }, t)));
    body.append(h('h4', {}, 'Practice'), h('div', { class: 'panel' },
        h('div', { class: 'row' }, h('span', { class: 'grow' }, 'Cards'), practice),
        checkRow('Shuffle', prefs.shuffle, (on) => { setPref('shuffle', on); rebuild(); }),
        h('button', { class: 'menu-btn', onclick: () => { rebuild(); closeDrawer(); } }, '↺ Restart from the first card')));

    const counts = {};
    for (const c of deck.cards) if (matchesKind(c)) counts[groupKey(c.src, c.group)] = (counts[groupKey(c.src, c.group)] || 0) + 1;
    const selected = selectedSet();
    const toggle = (keys, on) => {
        for (const k of keys) on ? selected.add(k) : selected.delete(k);
        setSelected(selected);
        rebuild();
    };
    body.append(h('h4', {}, 'Study these'));
    for (const source of deck.sources) {
        const keys = source.groups.map((g) => groupKey(source.id, g.id));
        const collapsed = prefs.collapsed.includes(source.id);
        const count = keys.filter((k) => selected.has(k)).length;
        body.append(h('div', { class: 'panel', style: 'margin-bottom:10px' },
            h('button', {
                class: 'source-head' + (collapsed ? ' collapsed' : ''),
                onclick: () => {
                    const set = new Set(prefs.collapsed);
                    collapsed ? set.delete(source.id) : set.add(source.id);
                    setPref('collapsed', [...set]);
                    renderDrawer();
                },
            }, h('span', { class: 'chev' }, '▾'), source.title, h('span', { class: 'count' }, `${count}/${keys.length}`)),
            !collapsed && h('div', { class: 'links' },
                h('button', { onclick: () => toggle(keys, true) }, 'Select all'),
                h('button', { onclick: () => toggle(keys, false) }, 'Clear')),
            !collapsed && source.groups.map((g, i) =>
                checkRow(g.label, selected.has(keys[i]), (on) => toggle([keys[i]], on), counts[keys[i]] || 0))));
    }

    body.append(h('h4', {}, 'More'), h('div', { class: 'panel' },
        (deck.extras || []).map((x) => h('button', {
            class: 'menu-btn',
            onclick: () => window.open(x.href, '_blank', 'noopener'),
        }, x.label)),
        h('button', { class: 'menu-btn', onclick: () => { closeDrawer(); openPrint(); } }, '🖨 Print / Save as PDF'),
        h('button', { class: 'menu-btn', onclick: exportNotes, disabled: !Object.keys(notes.all).length },
            `⤓ Export my notes (${Object.keys(notes.all).length})`),
        h('button', {
            class: 'menu-btn danger',
            onclick: () => {
                if (!confirm('Clear every Known/Review mark and the review schedule?')) return;
                progress.reset();
                rebuild();
            },
        }, 'Reset progress')));

    $('#drawer-foot').textContent = `${session.order.length} ${NOUNS[prefs.kind]} selected`;
    body.scrollTop = scroll;
}

// ---- Notes ----

function openNote(card) {
    const dialog = $('#note-dialog');
    const area = h('textarea', { spellcheck: 'true' }, notes.all[card.id] || '');
    const close = () => { dialog.close(); render(); };
    dialog.replaceChildren(
        h('div', { class: 'dialog-body' }, h('h2', {}, `Note — ${card.label}`), area),
        h('div', { class: 'dialog-actions' },
            notes.all[card.id] && h('button', { class: 'btn bad', onclick: () => { notes.set(card.id, ''); close(); } }, 'Delete'),
            h('button', { class: 'btn', onclick: () => dialog.close() }, 'Cancel'),
            h('button', { class: 'btn primary', onclick: () => { notes.set(card.id, area.value); close(); } }, 'Save')));
    dialog.showModal();
    area.focus();
}

function exportNotes() {
    const byId = Object.fromEntries(deck.cards.map((c) => [c.id, c]));
    const plain = (html) => html.replace(/<[^>]+>/g, '');
    let out = '# GenL Cards — my notes\n\n';
    for (const id of Object.keys(notes.all).sort()) {
        const c = byId[id];
        out += `## ${c ? c.label : id}\n\n${c ? plain(c.front) : ''}\n\n${notes.all[id]}\n\n`;
    }
    const a = h('a', { href: URL.createObjectURL(new Blob([out], { type: 'text/markdown' })), download: 'genl-notes.md' });
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
}

// ---- Print / PDF ----

function cardsToPrint(opts) {
    const cards = selectedCards();
    return opts.reviewOnly ? cards.filter((c) => progress.review.has(c.id)) : cards;
}

function openPrint() {
    if (!deck) return;
    const dialog = $('#print-dialog');
    const opts = { ...prefs.print };
    const countLine = h('p', {});
    const printBtn = h('button', { class: 'btn primary', onclick: () => { dialog.close(); printCards(opts); } },
        'Print / Save as PDF');
    const update = () => {
        setPref('print', { ...opts });
        const n = cardsToPrint(opts).length;
        countLine.textContent = n
            ? `${n} card${n === 1 ? '' : 's'} from the groups ticked in the menu. In the print screen, choose “Save as PDF” to make a PDF.`
            : 'No cards to print. Tick some groups in the menu, or turn off “Only cards marked for review”.';
        printBtn.disabled = n === 0;
    };
    const opt = (key, label) => checkRow(label, opts[key], (on) => { opts[key] = on; update(); });
    dialog.replaceChildren(
        h('div', { class: 'dialog-body' },
            h('h2', {}, 'Print cards'),
            countLine,
            h('div', { class: 'panel' },
                opt('answers', 'Include answers and explanations'),
                opt('notes', 'Include my notes'),
                opt('reviewOnly', 'Only cards marked for review'))),
        h('div', { class: 'dialog-actions' },
            h('button', { class: 'btn', onclick: () => dialog.close() }, 'Cancel'),
            printBtn));
    update();
    dialog.showModal();
}

function printCards(opts) {
    const cards = cardsToPrint(opts);
    const sources = Object.fromEntries(deck.sources.map((s) => [s.id, s]));
    const heading = (c) => {
        const s = sources[c.src];
        const g = s && s.groups.find((x) => x.id === c.group);
        return s ? `${s.title} — ${g ? g.label : c.group}` : c.src;
    };
    const kind = KINDS.find(([v]) => v === prefs.kind)[1];
    const title = `NCP-GENL — ${kind}`;
    GLCard.renderPrint($('#print-area'), cards, {
        title, answers: opts.answers, notes: opts.notes ? notes.all : {}, heading,
    });
    const oldTitle = document.title;
    document.title = title;
    window.addEventListener('afterprint', () => { document.title = oldTitle; }, { once: true });
    setTimeout(() => window.print(), 300);
}

// ---- Wiring ----

$('#kind-switch').addEventListener('click', (e) => {
    const value = e.target.closest('button')?.dataset.value;
    if (!value || value === prefs.kind || !deck) return;
    setPref('kind', value);
    rebuild();
});
$('#study-switch').addEventListener('click', (e) => {
    const value = e.target.closest('button')?.dataset.value;
    if (!value || value === prefs.study || !deck) return;
    setPref('study', value);
    rebuild();
});
$('#open-drawer').addEventListener('click', openDrawer);
$('#close-drawer').addEventListener('click', closeDrawer);
$('#backdrop').addEventListener('click', closeDrawer);
$('#open-print').addEventListener('click', openPrint);

document.addEventListener('keydown', (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey) {
        if ((e.metaKey || e.ctrlKey) && e.key === 'p' && deck) {
            e.preventDefault();
            openPrint();
        }
        return;
    }
    if (e.key === 'Escape') { closeDrawer(); return; }
    if (document.querySelector('dialog[open]') || e.target.closest?.('input, textarea, select')) return;
    const card = deck && !session.finished ? currentCard() : null;
    if (!card) return;
    const test = prefs.study === 'test';
    const key = e.key.length === 1 ? e.key.toLowerCase() : e.key;
    const actions = {
        ArrowLeft: () => move(-1),
        ArrowRight: () => move(1),
        ' ': () => (isQuestion(card) && revealed(card) && test ? advance() : reveal()),
        g: () => test && grade(true),
        m: () => test && grade(false),
        k: () => { if (!test) { progress.toggleKnown(card.id); render(); } },
        r: () => { if (!test) { progress.toggleReview(card.id); render(); } },
        n: () => openNote(card),
        o: () => card.link && window.open(card.link, '_blank', 'noopener'),
    };
    if (isQuestion(card)) for (const o of card.options) actions[o.key.toLowerCase()] = () => choose(o.key);
    const run = actions[key];
    if (run) {
        e.preventDefault();
        run();
    }
});

render();

fetch('deck.json')
    .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
    })
    .then((data) => {
        deck = data;
        rebuild();
    })
    .catch((err) => {
        loadError = `Open this page once while online so the cards can be saved for offline use. (${err.message})`;
        render();
    });

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
}
