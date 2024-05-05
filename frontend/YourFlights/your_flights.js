document.getElementById('checkInButton').addEventListener('click', function() {
    fetch('/checkin_clicked', {method: 'POST'})
    .then(function(response) {
        if(response.ok) {
            return response.json();
        }
        throw new Error('Request failed.');
    })
    .then(function(data) {
        if(data.message === 'Voluntario') {
            //llamamos a CheckIn_voluntario
            window.location.href = '../CheckIn_voluntario/checkin.html';
        }
        else {
            //llamamos a CheckIn_invident
            window.location.href = '../CheckIn_invidente/checkin.html';

        }        
    })
    .catch(function(error) {
        console.log(error);
    });
});