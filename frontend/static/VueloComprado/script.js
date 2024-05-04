// make me a script that grabs the <p> from the DOM and requests the data from 127.0.0.1:5000/numero and displays the response inside the p element.

// Assuming you have an HTML structure like this:
// <p id="data"></p>

// Grab the <p> element from the DOM
const paragraph = document.getElementById('parrafo');

// Function to make the request and update the <p> element with the response
async function fetchData() {
    try {
        // Make a request to 127.0.0.1:5000/numero
        const response = await fetch('http://127.0.0.1:5000/numero');
        
        // Check if the request was successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Parse the response as JSON
        const data = await response.json();

        // Update the <p> element with the response
        paragraph.textContent = data.number;
    } catch (error) {
        // Handle errors
        console.error('There was a problem fetching the data:', error);
    }
}

// Call the fetchData function when the script is loaded
fetchData();
