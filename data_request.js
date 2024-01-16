// Jede Sekunde wird die Zeit aktualisiert
// alle 5 Sekunden werden die Daten neu vom Server abgefragt

// jede Sekunde wird setTime aufgerufen
window.setInterval(setTime, 1000)
window.setInterval(getData, 5000)

function setTime()
{
    var time = new Date().toLocaleTimeString();
    document.getElementById("time").innerText = time;
}

async function getData()
{
    const data = await fetch("http://localhost:1111/data");
    const result = await data.json();
    writeDataIntoWebsite(result);
}

async function writeDataIntoWebsite(data)
{
    document.getElementById("room").innerText = data.room;
    document.getElementById("temperature").innerText = data.temp;
    document.getElementById("humid").innerText = data.water;
    document.getElementById("temperature_limit").innerText = data.tlimit;
}