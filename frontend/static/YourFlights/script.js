document.addEventListener('DOMContentLoaded', function() {
    fetch('http://barrierfreeboarding.co:5001/lista_vuelos')
        .then(response => response.json())
        .then(data => {
            const vuelos = data.vuelos;
            const listaVuelos = document.querySelector('.flight-list');
            vuelos.forEach(vuelo => {
                const divVuelo = document.createElement('div');
                divVuelo.className = 'flight';
                divVuelo.innerHTML = `
                    <td">${vuelo[0]}</td>
                    <td">${vuelo[1]}</td>
                    <td">${vuelo[2]}</td>
                    <td">${vuelo[3]}</td>
                    <td">${vuelo[4]}</td>
                `;
                listaVuelos.appendChild(divVuelo);
            });
        })
        .catch(error => console.error('Error loading the flight data:', error));
});

document.addEventListener("DOMContentLoaded", function() {
    const flights = document.querySelectorAll('tr:not(:first-child)');  // Excluye el encabezado de la tabla

    flights.forEach(flight => {
        const dateString = flight.cells[3].textContent;  // "10/5/2024 10:00"
        const [date, time] = dateString.split(' ');
        const [day, month, year] = date.split('/');
        const [hours, minutes] = time.split(':');
        
        const flightDate = new Date(year, month - 1, day, hours, minutes);
        const now = new Date();
        const timeDiff = flightDate.getTime() - now.getTime();
        const hoursDiff = timeDiff / (1000 * 60 * 60); // Convertir a horas

        const checkinButton = flight.querySelector('.button-checkin');
        const drawButton = flight.querySelector('.button-draw');

        if (hoursDiff <= 48 && hoursDiff > 0) {
            checkinButton.disabled = false;
        } else {
            checkinButton.disabled = true;
        }

        if (flightDate < now) { // El vuelo ya pasó
            drawButton.disabled = false;
        } else {
            drawButton.disabled = true;
        }
    });
});
