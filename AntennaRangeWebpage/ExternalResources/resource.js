$(document).ready(function() {
    $(function() {
        $("#navbar").load("../NavBar/nav.html", function() {
            $("#Resources").addClass("navButton active").removeClass("navButton");
        });
    })
})