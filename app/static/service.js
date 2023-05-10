if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
    navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
        // Service Worker registrado com sucesso
        console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, function(err) {
        // Erro ao registrar o Service Worker
        console.log('ServiceWorker registration failed: ', err);
    });
    });
}