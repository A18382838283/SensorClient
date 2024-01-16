// Jede Sekunde wird die Zeit aktualisiert
// alle 5 Sekunden werden die Daten neu vom Server abgefragt

// jede Sekunde wird setTime aufgerufen
window.setInterval(setTime, 1000)

function setTime()
{
    var time = new Date().toLocaleTimeString();
    document.getElementById("time").innerText = time;
}