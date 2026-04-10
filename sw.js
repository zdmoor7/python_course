self.addEventListener('install', e => e.waitUntil(
    caches.open('insulin-v1').then(cache => cache.addAll(['/']))
));

self.addEventListener('fetch', e => {
    e.respondWith(
        fetch(e.request).catch(() => caches.match(e.request))
    );
});
