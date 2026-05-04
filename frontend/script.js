let city = document.getElementById("city");
let btn = document.getElementById("btn");
let result = document.getElementById("result");


function getWeather(){
    const cityName = city.value.trim();


    if (!cityName){
        result.innerHTML = "Please enter a city";
        return;
    }

    result.innerHTML = `<div class="loading">Loading...</div>`;

    fetch(`http://127.0.0.1:8000/weather/?city=${cityName}`)
    .then(response=> {
        if (response.ok === false){
            throw new Error("City not found")
        }
        return response.json();
    })
    .then(data=> result.innerHTML = `
    <div class="weather-card">
        <div class="city">${data.city}</div>
        <div class="temp">${data.temperature}°C</div>
        <div class="condition">${data.condition}</div>
    </div>
`)
    .catch(error=>result.innerHTML = `<div class="error">${error.message}</div>`);
}


btn.addEventListener("click", getWeather)


city.addEventListener("keydown", (e) => {
    if (e.key === "Enter"){
    getWeather();
}})