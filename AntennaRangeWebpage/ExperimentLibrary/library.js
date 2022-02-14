$(document).ready(function() {
    $(function() {
        $("#navbar").load("../NavBar/nav.html", function() {
            $("#Library").addClass("navButton active").removeClass("navButton");
        });
    })
})