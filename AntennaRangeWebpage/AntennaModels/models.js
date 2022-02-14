$(document).ready(function() {
    $(function() {
        $("#navbar").load("../NavBar/nav.html", function() {
            $("#Models").addClass("navButton active").removeClass("navButton");
        });
    })
})

function changeModel(modelPath) {
    document.getElementById('x3dModel1').setAttribute('url', modelPath);
    x3dom.reload();
}


function search() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}



// functions for the popup info
function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}

function updatePopup(id) {
    var popup = document.getElementById(id);
    if (popup.style.display == 'block')
        popup.style.display = 'none';
    else
        popup.style.display = 'block';
}
