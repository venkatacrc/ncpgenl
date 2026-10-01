'use strict';

// Renders one GenL card (or a printable list of cards) into a DOM element. Shared by the
// Mac app (WKWebView, card.html) and the phone/web app (web/app.js); the host sets
// GLCard.onEvent to receive 'flip', 'choose' and 'link' events.
(function () {
    const KIND_NAMES = {
        lesson: 'Lesson', concept: 'Concept', verse: 'Verse', question: 'Question', trap: 'Trap', reading: 'Reading',
    };

    function h(tag, attrs = {}, ...children) {
        const el = document.createElement(tag);
        for (const [k, v] of Object.entries(attrs)) {
            if (v == null || v === false) continue;
            if (k === 'class') el.className = v;
            else if (k === 'html') el.innerHTML = v;
            else if (k.startsWith('on')) el.addEventListener(k.slice(2), v);
            else el.setAttribute(k, v === true ? '' : v);
        }
        for (const c of children.flat()) {
            if (c == null || c === false) continue;
            el.append(c instanceof Node ? c : String(c));
        }
        return el;
    }

    const emit = (type, data) => { if (GLCard.onEvent) GLCard.onEvent(type, data); };

    function typeset(root) {
        if (window.renderMathInElement) {
            window.renderMathInElement(root, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '\\(', right: '\\)', display: false },
                    { left: '$', right: '$', display: false },
                ],
                throwOnError: false,
                strict: 'ignore',
            });
        }
        if (window.Prism) window.Prism.highlightAllUnder(root);
        for (const a of root.querySelectorAll('a[href]')) {
            a.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                emit('link', a.href);
            });
        }
    }

    function badges(card, state) {
        return h('div', { class: 'gl-badges' },
            h('span', { class: 'gl-label' }, card.label,
                card.meta && card.kind !== 'reading' ? h('span', { class: 'gl-meta' }, card.meta) : null),
            h('span', { class: 'gl-chip kind-' + card.kind }, KIND_NAMES[card.kind] || card.kind),
            state.known && h('span', { class: 'gl-chip known' }, 'Known'),
            state.review && h('span', { class: 'gl-chip review' }, 'Review'),
            state.box ? h('span', { class: 'gl-chip box', title: 'Spaced-repetition box' }, `Box ${state.box}`) : null,
            state.note && h('span', { class: 'gl-chip note' }, 'Note'));
    }

    function block(title, html, cls = '') {
        return h('section', { class: 'gl-block ' + cls },
            h('h3', {}, title),
            h('div', { class: 'gl-md', html }));
    }

    function options(card, state, revealed) {
        return h('ol', { class: 'gl-options' }, card.options.map((o) => {
            let cls = 'gl-option';
            if (revealed && o.key === card.answer) cls += ' correct';
            if (revealed && state.chosen === o.key && o.key !== card.answer) cls += ' wrong';
            if (state.chosen === o.key) cls += ' chosen';
            return h('li', {
                class: cls,
                onclick: (e) => { e.stopPropagation(); if (!revealed) emit('choose', o.key); },
            }, h('span', { class: 'gl-key' }, o.key), h('span', { class: 'gl-md', html: o.html }));
        }));
    }

    /**
     * state: { flipped, known, review, box, note, chosen, hint, test }
     * `flipped` shows the back; for questions it also marks the right option.
     */
    function render(root, card, state = {}) {
        const flipped = !!state.flipped;
        const el = h('article', { class: `gl-card kind-${card.kind}` + (flipped ? ' flipped' : '') });
        el.append(badges(card, state));
        if (card.cue) el.append(h('div', { class: 'gl-cue gl-md', html: card.cue }));
        el.append(h('div', { class: 'gl-front gl-md', html: card.front }));
        if (card.kind === 'question' && card.options) el.append(options(card, state, flipped));

        if (flipped) {
            el.append(h('hr', { class: 'gl-rule' }));
            if (card.kind === 'question') {
                const verdict = state.chosen
                    ? (state.chosen === card.answer ? `✓ ${state.chosen} is correct` : `✗ You chose ${state.chosen} — the answer is ${card.answer}`)
                    : `Answer: ${card.answer}`;
                el.append(h('div', {
                    class: 'gl-verdict ' + (state.chosen ? (state.chosen === card.answer ? 'good' : 'bad') : ''),
                }, verdict));
            }
            for (const b of card.back || []) el.append(block(b.title, b.html, b.cls || ''));
            if (card.link) {
                el.append(h('p', { class: 'gl-linkrow' },
                    h('a', { href: card.link }, 'Open ' + (card.linkLabel || 'link') + ' ↗')));
            }
            if (state.note) el.append(block('My note', escapeHtml(state.note).replace(/\n/g, '<br>'), 'note'));
        } else if (state.hint) {
            el.append(h('div', { class: 'gl-hint' }, state.hint));
        }
        el.addEventListener('click', (e) => {
            if (e.target.closest('a, .gl-option, pre, code')) return;
            if (window.getSelection && String(window.getSelection()).length) return;
            emit('flip');
        });
        root.replaceChildren(el);
        typeset(el);
        return el;
    }

    function escapeHtml(s) {
        return String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
    }

    /** opts: { title, answers, notes: {id: text}, heading: (card) => string } */
    function renderPrint(root, cards, opts) {
        const doc = h('div', { class: 'gl-print' },
            h('h1', {}, opts.title),
            h('div', { class: 'gl-print-count' }, `${cards.length} card${cards.length === 1 ? '' : 's'}`));
        let last = null;
        for (const card of cards) {
            const head = opts.heading ? opts.heading(card) : '';
            if (head && head !== last) {
                doc.append(h('h2', {}, head));
                last = head;
            }
            const item = h('div', { class: 'gl-print-card' },
                h('div', { class: 'gl-print-label' }, card.label),
                card.cue && h('div', { class: 'gl-cue gl-md', html: card.cue }),
                h('div', { class: 'gl-front gl-md', html: card.front }));
            if (card.kind === 'question' && card.options) {
                item.append(h('ol', { class: 'gl-options print' }, card.options.map((o) =>
                    h('li', { class: 'gl-option' + (opts.answers && o.key === card.answer ? ' correct' : '') },
                        h('span', { class: 'gl-key' }, o.key), h('span', { class: 'gl-md', html: o.html })))));
            }
            if (opts.answers) {
                if (card.kind === 'question') item.append(h('div', { class: 'gl-verdict' }, `Answer: ${card.answer}`));
                for (const b of card.back || []) item.append(block(b.title, b.html, b.cls || ''));
                if (card.link) item.append(h('p', { class: 'gl-linkrow' }, card.link));
            }
            const note = opts.notes && opts.notes[card.id];
            if (note) item.append(block('My note', escapeHtml(note).replace(/\n/g, '<br>'), 'note'));
            doc.append(item);
        }
        root.replaceChildren(doc);
        typeset(doc);
        return doc;
    }

    window.GLCard = { render, renderPrint, onEvent: null, kindNames: KIND_NAMES };
})();
