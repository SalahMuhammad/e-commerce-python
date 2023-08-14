// service-worker.js

const CACHE_NAME = 'my-site-cache-v1';
const urlsToCache = [
  '/',
  // '{% static "css/style.css" %}',
//   '/js/script.js',
//   '/images/logo.png',
  // Add other URLs to cache
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => response || fetch(event.request))
  );
});
