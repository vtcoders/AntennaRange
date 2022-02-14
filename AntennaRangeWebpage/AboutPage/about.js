$(document).ready(function() {
    $(function() {
        $("#navbar").load("../NavBar/nav.html", function() {
            $("#About").addClass("navButton active").removeClass("navButton");
        });
    })
})