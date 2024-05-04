document.addEventListener('DOMContentLoaded', function() {
    fetch('')
        .then(response => response.json())
        .then(data => {
            const vuelos = data.vuelos;
            const listaVuelos = document.querySelector('.flight-list');
            vuelos.forEach(vuelo => {
                const divVuelo = document.createElement('div');
                divVuelo.className = 'flight';
                divVuelo.innerHTML = `
                    <span class="flight-number">${vuelo.numero}</span>
                    <span class="flight-origin">${vuelo.origen}</span>
                    <span class="flight-destination">${vuelo.destino}</span>
                    <span class="flight-date">${vuelo.fecha}</span>
                    <span class="flight-terminal">${vuelo.terminal}</span>
                `;
                listaVuelos.appendChild(divVuelo);
            });
        })
        .catch(error => console.error('Error loading the flight data:', error));
});
