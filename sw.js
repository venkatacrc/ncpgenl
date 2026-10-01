"use strict";
/* Decrypts Instant-Lock-style IAGP blobs. Scope-aware for GitHub Pages subpaths. */
const MAGIC = new Uint8Array([0x49, 0x41, 0x47, 0x50]);
const SALT_LEN = 16, IV_LEN = 12, ITER = 100000;
const MIME = {
  html: 'text/html; charset=utf-8', htm: 'text/html; charset=utf-8',
  css: 'text/css; charset=utf-8', js: 'text/javascript; charset=utf-8', mjs: 'text/javascript; charset=utf-8',
  json: 'application/json; charset=utf-8', webmanifest: 'application/manifest+json',
  svg: 'image/svg+xml', png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', gif: 'image/gif',
  woff: 'font/woff', woff2: 'font/woff2', ttf: 'font/ttf', ico: 'image/x-icon', map: 'application/json',
  txt: 'text/plain; charset=utf-8', md: 'text/plain; charset=utf-8',
};
let password = null;

async function deriveKey(pw, salt) {
  const base = await crypto.subtle.importKey('raw', new TextEncoder().encode(pw), 'PBKDF2', false, ['deriveKey']);
  return crypto.subtle.deriveKey(
    { name: 'PBKDF2', salt, iterations: ITER, hash: 'SHA-256' },
    base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
}

async function decrypt(buf, pw) {
  const u8 = buf instanceof Uint8Array ? buf : new Uint8Array(buf);
  for (let i = 0; i < 4; i++) if (u8[i] !== MAGIC[i]) throw new Error('not encrypted');
  const salt = u8.slice(4, 4 + SALT_LEN);
  const iv = u8.slice(4 + SALT_LEN, 4 + SALT_LEN + IV_LEN);
  const data = u8.slice(4 + SALT_LEN + IV_LEN);
  const key = await deriveKey(pw, salt);
  return crypto.subtle.decrypt({ name: 'AES-GCM', iv }, key, data);
}

function underScope(pathname) {
  const base = new URL(self.registration.scope).pathname.replace(/\/$/, '');
  if (!base) return pathname === '/' || pathname.startsWith('/');
  return pathname === base || pathname.startsWith(base + '/');
}

function rewritePath(pathname) {
  const scopePath = new URL(self.registration.scope).pathname; // ends with /
  if (pathname === scopePath || pathname === scopePath + 'index.html') {
    return scopePath + '__index.html';
  }
  return pathname;
}

self.addEventListener('install', (e) => e.waitUntil(self.skipWaiting()));
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));
self.addEventListener('message', async (ev) => {
  const data = ev.data || {};
  if (data.type === 'CLAIM') { await self.clients.claim(); return; }
  if (data.type === 'SET_PASSWORD') {
    const pw = data.password || '';
    try {
      // Prove the password by decrypting __index.html under this scope.
      const probe = await fetch(new URL('__index.html', self.registration.scope));
      const buf = await probe.arrayBuffer();
      await decrypt(buf, pw);
      password = pw;
      ev.ports?.[0]?.postMessage({ ok: true });
    } catch (err) {
      password = null;
      ev.ports?.[0]?.postMessage({ ok: false, error: 'Wrong password' });
    }
  }
});

self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin || !password || !underScope(url.pathname)) return;
  // Never try to decrypt the unlock SW or the gate page itself mid-flight in a loop;
  // the gate is plaintext index.html — rewrite to __index.html instead.
  const path = rewritePath(url.pathname);
  const target = new URL(path, url.origin);
  // Leave the plaintext sw.js and gate alone when asked directly before rewrite — sw is never encrypted.
  if (path.endsWith('/sw.js')) return;
  event.respondWith((async () => {
    const res = await fetch(target, { cache: 'no-store' });
    if (!res.ok) return res;
    const buf = new Uint8Array(await res.arrayBuffer());
    const isEnc = buf.length >= 4 && buf[0] === MAGIC[0] && buf[1] === MAGIC[1] && buf[2] === MAGIC[2] && buf[3] === MAGIC[3];
    if (!isEnc) return new Response(buf, { status: res.status, headers: res.headers });
    try {
      const plain = await decrypt(buf, password);
      const ext = path.split('.').pop()?.toLowerCase() || '';
      const type = MIME[ext] || 'application/octet-stream';
      return new Response(plain, { status: 200, headers: { 'Content-Type': type, 'Cache-Control': 'no-store' } });
    } catch (err) {
      console.error('decrypt failed', err);
      return new Response('Decryption failed', { status: 403 });
    }
  })());
});
