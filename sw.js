// sw.js
self.addEventListener('install', event => {
    console.log('Service Worker installé.');
    // Activation immédiate
    self.skipWaiting();
});

self.addEventListener('activate', event => {
    console.log('Service Worker activé.');
});

self.addEventListener('fetch', event => {
    // Ici tu peux gérer le cache si tu veux, sinon juste laisser passer
    // console.log('Fetch intercepté : ', event.request.url);
});
