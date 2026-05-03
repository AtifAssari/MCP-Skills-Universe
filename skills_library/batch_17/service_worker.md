---
title: service-worker
url: https://skills.sh/jgamaraalv/ts-dev-kit/service-worker
---

# service-worker

skills/jgamaraalv/ts-dev-kit/service-worker
service-worker
Installation
$ npx skills add https://github.com/jgamaraalv/ts-dev-kit --skill service-worker
SKILL.md
Service Worker
Table of Contents
Constraints
Lifecycle
Registration
Install / Activate / Fetch Events
Common Pitfalls
Next.js Integration
Reference files
Constraints
HTTPS required (localhost exempt for dev)
No DOM access — runs on separate thread
Fully async — no synchronous XHR, no localStorage
No dynamic import() — only static import statements
Scope defaults to the directory containing the SW file
self refers to ServiceWorkerGlobalScope

<quick_reference>

Lifecycle
register() → Download → Install → [Wait] → Activate → Fetch control

Register from main thread via navigator.serviceWorker.register()
Install event fires once — use to pre-cache static assets
Wait — new SW waits until all tabs using old SW are closed (skip with self.skipWaiting())
Activate event fires — use to clean up old caches
Fetch events start flowing — SW controls page network requests

A document must reload to be controlled (or call clients.claim() during activate).

Updating a Service Worker
Browser byte-compares the SW file on each navigation (or every 24h)
New version installs in background while old version still serves
Increment the cache name (e.g., v1 → v2) in the new version
Delete old caches in the activate handler
Call self.skipWaiting() in install to activate immediately
Call self.clients.claim() in activate to take control of open pages
DevTools
Chrome: chrome://inspect/#service-workers or Application > Service Workers
Firefox: about:debugging#/runtime/this-firefox or Application > Service Workers
Edge: edge://inspect/#service-workers or Application > Service Workers

Unregister, update, and inspect caches from the Application panel. Use "Update on reload" checkbox during development.

</quick_reference>

Registration
// main.js — register from the page
if ("serviceWorker" in navigator) {
  const reg = await navigator.serviceWorker.register("/sw.js", { scope: "/" });
  // reg.installing | reg.waiting | reg.active
}


Scope rules:

SW at /sw.js can control / and all subpaths
SW at /app/sw.js can only control /app/ by default
Broaden scope with Service-Worker-Allowed response header
Install Event — Pre-cache Assets
// sw.js
const CACHE_NAME = "v1";
const PRECACHE_URLS = ["/", "/index.html", "/style.css", "/app.js"];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE_URLS)));
});


waitUntil(promise) — keeps install phase alive until the promise settles. If rejected, installation fails and the SW won't activate.

Activate Event — Clean Up Old Caches
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))),
      ),
  );
});

Fetch Event — Intercept Requests
self.addEventListener("fetch", (event) => {
  event.respondWith(caches.match(event.request).then((cached) => cached || fetch(event.request)));
});


respondWith(promise) — must be called synchronously (within the event handler, not in a microtask). The promise resolves to a Response.

For caching strategy patterns (cache-first, network-first, stale-while-revalidate), see references/caching-strategies.md.

Navigation Preload

Avoid the startup delay when a SW boots to handle a navigation:

self.addEventListener("activate", (event) => {
  event.waitUntil(self.registration?.navigationPreload.enable());
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    (async () => {
      const cached = await caches.match(event.request);
      if (cached) return cached;

      const preloaded = await event.preloadResponse;
      if (preloaded) return preloaded;

      return fetch(event.request);
    })(),
  );
});

Communicating with Pages
// Page → SW
navigator.serviceWorker.controller.postMessage({ type: "SKIP_WAITING" });

// SW → Page (via Clients API)
const clients = await self.clients.matchAll({ type: "window" });
clients.forEach((client) => client.postMessage({ type: "UPDATED" }));

// SW listens
self.addEventListener("message", (event) => {
  if (event.data?.type === "SKIP_WAITING") self.skipWaiting();
});

Next.js Integration

In Next.js, place the service worker file in public/sw.js. public/sw.js is intentionally plain JS (not processed by Next.js build pipeline). Register it from a client component:

"use client";
import { useEffect } from "react";

export function ServiceWorkerRegistrar() {
  useEffect(() => {
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker.register("/sw.js");
    }
  }, []);
  return null;
}


Add to root layout. Next.js serves public/ files at the root, so /sw.js scope covers /.

Common Pitfalls
Response cloning — response.clone() before both caching and returning, since body streams can only be read once
Opaque responses — cross-origin fetches without CORS return opaque responses (status 0). cache.add() will refuse them. Use cache.put() but you can't inspect the response
waitUntil timing — call event.waitUntil() synchronously within the event handler, not inside an async callback
Scope ceiling — a SW cannot control URLs above its own directory unless Service-Worker-Allowed header is set
No state persistence — the SW may terminate at any time when idle. Don't store state in global variables — use Cache API or IndexedDB
Reference files
Caching strategies (cache-first, network-first, stale-while-revalidate): references/caching-strategies.md
Push notifications & background sync (push subscription, push events, background sync): references/push-and-sync.md
API quick reference (Cache, CacheStorage, FetchEvent, Clients, ServiceWorkerRegistration, ServiceWorkerGlobalScope): references/api-reference.md
Weekly Installs
24
Repository
jgamaraalv/ts-dev-kit
GitHub Stars
14
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn