let city = document.getElementById("city");
let btn = document.getElementById("btn");
let result = document.getElementById("result");

btn.addEventListener("click", () => {
    fetch(`http://127.0.0.1:8000/weather/?city=${city.value}`)
    .then(response=>response.json())
    .then(data=> result.innerHTML = "City: " + data.city + "<br>Temperature: " + data.temperature + "<br>Condition :" + data.condition)
    .catch(error=>console.error(error));
})
