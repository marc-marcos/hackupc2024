document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:5001/lista_vuelos')
        .then(response => response.json())
        .then(data => {
            const vuelos = data.vuelos;
            const listaVuelos = document.querySelector('.flight-list');
            vuelos.forEach(vuelo => {
                const divVuelo = document.createElement('div');
                divVuelo.className = 'flight';
                divVuelo.innerHTML = `
                    <span class="flight-number">${vuelo[0]}</span>
                    <span class="flight-origin">${vuelo[1]}</span>
                    <span class="flight-destination">${vuelo[2]}</span>
                    <span class="flight-date">${vuelo[3]}</span>
                    <span class="flight-time">${vuelo[4]}</span>
                `;
                listaVuelos.appendChild(divVuelo);
            });
        })
        .catch(error => console.error('Error loading the flight data:', error));
});
