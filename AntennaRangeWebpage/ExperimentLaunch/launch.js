$(document).ready(function() {
    $(function() {
        $("#navbar").load("../NavBar/nav.html", function() {
            $("#Launch").addClass("navButton active").removeClass("navButton");
        });
    })
})