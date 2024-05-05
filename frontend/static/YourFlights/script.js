document.addEventListener('DOMContentLoaded', function () {
    fetch('http://barrierfreeboarding.co:5001/lista_vuelos')
        .then(response => response.json())
        .then(data => {
            const vuelos = data.vuelos;
            const listaVuelos = document.querySelector('.main-content table tbody');
            vuelos.forEach(vuelo => {
                const trVuelo = document.createElement('tr');
                trVuelo.className = 'flight';

                const fechaVuelo = new Date(vuelo.fecha + 'T' + vuelo.hora); // Asegúrate de que la fecha y la hora estén en formato reconocible
                const ahora = new Date();
                const diff = fechaVuelo - ahora;
                const horasRestantes = diff / (1000 * 60 * 60); // Convertir de milisegundos a horas

                trVuelo.innerHTML = `
                    <td>${vuelo[0]}</td>
                    <td>${vuelo[1]}</td>
                    <td>${vuelo[2]}</td>
                    <td>${vuelo[3].toLocaleString()}</td>
                    <td>${vuelo[4]}</td>
                    <td>
                        <button class="button-checkin" ${horasRestantes > 0 && horasRestantes <= 48 ? '' : 'disabled'} onclick="location.href='/check_in';">Check in</button>
                    </td>
                    <td>
                        <button class="button-draw" ${fechaVuelo < ahora ? '' : 'disabled'} onclick="location.href='/roulete';">Claim your Draw</button>
                    </td>
                `;
                listaVuelos.appendChild(trVuelo);
            });
        })
        .catch(error => console.error('Error loading the flight data:', error));
});




document.addEventListener("DOMContentLoaded", function () {
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

        if (flightDate.getTime() < now.getTime()) { // El vuelo ya pasó
            drawButton.removeAttribute("disabled");
        } else {
            drawButton.disabled = "";
        }
    });
});

document.getElementById('checkInButton').addEventListener('click', function() {
    fetch('/checkin_clicked', {method: 'POST'})
    .then(function(response) {
        if(response.ok) {
            return response.json();
        }
        throw new Error('Request failed.');
    })
    .then(function(data) {
        if(true) {
            //llamamos a CheckIn_voluntario
            window.location.href = '/checkin_voluntario';
        }
        else {
            //llamamos a CheckIn_invident
            window.location.href = '/checkin_invidente';

        }        
    })
    .catch(function(error) {
        console.log(error);
    });
});
