
// Here we are doing the D3 stuff to see if it works
d3.select("graphHome").append(“p”).text(“Our First Paragraph using D3!”);

// Beginning functions for visibility buttons and graphs?

function visibilityButtonClicked(button) {
    // Change class of visibility button for looks and filtering
    if (button.className === "visible") {
        button.className = "invisible";
        button.src = "./invisible.png";
    } // if
    else // button.className === "invisible"
    {
        button.className = "visible";
        button.src = "./visible.png";
    } // else
    graphsRefresh();
};

function graphsRefresh() {
    // for // look at eLibrary
};

function checkButtonClicked(button) {
    if (button.className === "visible") {
        button.className = "invisible";
        button.src = "./invisible.png";
    } // if
    else // button.className === "invisible"
    {
        button.className = "visible";
        button.src = "./visible.png";
    } // else
    graphsRefresh();
}

function dataRefresh() {

};

function allowDrop(ev) {
    ev.preventDefault();
};

function drag(ev) {
    ev.dataTransfer.setData("text/plain", ev.target.id);
};

function drop(ev) {
    justForExample = ["Experiment 1", "Feb 3, 2020", "35", "120.2", "132.23", "1.23"]
    divs = ev.target.getElementsByTagName('div');
    for (var i = 0; i < divs.length; i++) {
        divs[i].textContent = justForExample[i];
    }
    updateSliders(exp);
}

function updateSliders(experiment, mastAngle, armAngle, tRSSI, bRSSI) {

}

/**
function drop(ev) {
ev.preventDefault();
var data = ev.dataTransfer.getData("text");
ev.target.appendChild(document.getElementById(data));
ev.target.className = "column evenLeft blue";
};
**/
