---
rating: ⭐⭐⭐
title: progressive-web-app
url: https://skills.sh/secondsky/claude-skills/progressive-web-app
---

# progressive-web-app

skills/secondsky/claude-skills/progressive-web-app
progressive-web-app
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill progressive-web-app
SKILL.md
Progressive Web App (PWA)

Build web applications that work like native apps with offline support and installability.

Web App Manifest
{
  "name": "My Application",
  "short_name": "MyApp",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#000000",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/icon-512.png", "sizes": "512x512", "type": "image/png" }
  ]
}

Service Worker
const CACHE_NAME = 'app-v1';
const STATIC_ASSETS = ['/', '/index.html', '/styles.css', '/app.js'];

// Install
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS))
  );
});

// Fetch with cache-first strategy
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;

      return fetch(event.request).then(response => {
        if (response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      });
    })
  );
});

Install Prompt
let deferredPrompt;

window.addEventListener('beforeinstallprompt', e => {
  e.preventDefault();
  deferredPrompt = e;
  showInstallButton();
});

async function installApp() {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  const { outcome } = await deferredPrompt.userChoice;
  console.log('Install outcome:', outcome);
  deferredPrompt = null;
}

Push Notifications
async function subscribeToPush() {
  const registration = await navigator.serviceWorker.ready;
  const subscription = await registration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: VAPID_PUBLIC_KEY
  });
  await sendSubscriptionToServer(subscription);
}

PWA Checklist
 HTTPS enabled
 Web manifest configured
 Service worker registered
 Offline fallback page
 Responsive design
 Fast loading (<3s on 3G)
 Installable
Weekly Installs
178
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass