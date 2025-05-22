function fetchWeather() {
    let city = document.getElementById("city-input").value;
    
    if (city === "") {
        alert("Please enter a city name!");
        return;
    }

    fetch("/get_weather", {
        method: "POST",
        body: JSON.stringify({ city: city }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById("weather-result").innerHTML = `<p>${data.error}</p>`;
        } else {
            document.getElementById("city-name").innerText = data.city;
            document.getElementById("weather-icon").src = data.icon;
            document.getElementById("weather-description").innerText = data.description;
            document.getElementById("weather-temp").innerText = `Temperature: ${data.temperature}°C`;
        }
    })
    .catch(error => console.error("Error:", error));
}
