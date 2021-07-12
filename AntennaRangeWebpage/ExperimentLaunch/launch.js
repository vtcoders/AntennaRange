// used to change the value displayed in text box next to slider
function updateValue(id, val) {
    document.getElementById(id).value = val;
}

/**
* Updates the minimum value of the max angle when min is updated,
* changing the max angle when necessary
**/
function updateMaxFloor(id1, id2, val) {
    // set min
    document.getElementById(id1).setAttribute('min', val);
    // if current value is less than min, set it equal to min
    if (parseInt(document.getElementById(id1).value) < val) {
        document.getElementById(id1).setAttribute('value', val);
    }
    // repeat for the second element (the slider)
    document.getElementById(id2).setAttribute('min', val);
    if (parseInt(document.getElementById(id2).value) < val) {
        document.getElementById(id2).setAttribute('value', val);
    }

}

function updateDegPerStep(degId, maxValId, minValId, stepsId) {
    var difference = parseFloat(document.getElementById(maxValId).value) - parseFloat(document.getElementById(minValId).value);
    var steps = parseFloat(document.getElementById(stepsId).value);
    if (difference >= 1 && steps > 0) {
        document.getElementById(degId).value = (difference / steps).toFixed(2);
    }
    else {
        document.getElementById(degId).value = "Invalid";
    }
}

