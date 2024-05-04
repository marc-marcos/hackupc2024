
const loadingText = document.getElementById('loading-text');
let dotCount = 0;
const maxDots = 3;

function updateLoadingText() {
    let dots = '.'.repeat(dotCount);
    loadingText.textContent = `COMPRANDO VUELO${dots}`;
    dotCount = (dotCount + 1) % (maxDots + 1); // Volver a 0 después de 3 puntos
}    

// Actualizar el texto cada 0.5 segundos
const intervalId = setInterval(updateLoadingText, 500);

// Redireccionar después de 5 segundos
setTimeout(() => {
    clearInterval(intervalId); // Detener la animación
    window.location.href = '../VueloComprado/index.html'; // Cambiar a la nueva página
}, 5000);    

