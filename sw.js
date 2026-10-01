// Network first so a new deck or app version shows up as soon as the phone is online;
// the cache keeps everything working offline. KaTeX fonts are cached as they are used.
const CACHE = 'genl-cards-3ebc7c1cb0';
const FILES = [
    './',
    'index.html',
    'app.css',
    'app.js',
    'deck.json',
    'manifest.webmanifest',
    'icons/icon-192.png',
    'icons/icon-512.png',
    'icons/maskable-512.png',
    'cardkit/card.css',
    'cardkit/card.js',
    'cardkit/katex/katex.min.css',
    'cardkit/katex/katex.min.js',
    'cardkit/katex/contrib/auto-render.min.js',
    'cardkit/prism/prism-okaidia.min.css',
    'cardkit/prism/prism-core.min.js',
    'cardkit/prism/prism-clike.min.js',
    'cardkit/prism/prism-markup.min.js',
    'cardkit/prism/prism-python.min.js',
    'cardkit/prism/prism-bash.min.js',
    'cardkit/prism/prism-json.min.js',
    'cardkit/prism/prism-yaml.min.js',
];

self.addEventListener('install', (event) => {
    event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
            .then(() => self.clients.claim()));
});

self.addEventListener('fetch', (event) => {
    const { request } = event;
    if (request.method !== 'GET' || new URL(request.url).origin !== location.origin) return;
    event.respondWith(
        fetch(request)
            .then((response) => {
                if (response.ok) {
                    const copy = response.clone();
                    caches.open(CACHE).then((cache) => cache.put(request, copy));
                }
                return response;
            })
            .catch(() => caches.match(request, { ignoreSearch: true })));
});
