
document.addEventListener("DOMContentLoaded", function() {
    const flights = document.querySelectorAll('.flight');

    flights.forEach(flight => {
        const flightDateStr = flight.querySelector('.flight-date').textContent; // "24/10/2023 10:00"
        const flightDate = new Date(flightDateStr.split(' ')[0].split('/').reverse().join('-') + 'T' + flightDateStr.split(' ')[1]);

        const now = new Date();
        const timeDiff = flightDate - now; // Diferencia en milisegundos
        const hoursDiff = timeDiff / (1000 * 60 * 60); // Convertir a horas

        const checkinButton = flight.querySelector('.button-checkin');
        if (hoursDiff <= 48) {
            checkinButton.disabled = false; // Habilita el botón si quedan menos de 48 horas
            checkinButton.onclick = function() {
                window.location.href = 'https://pagina.com'; // Redirige a la página de check-in
            };
        } else {
            checkinButton.disabled = true; // Deja el botón desactivado
        }
    });
});

