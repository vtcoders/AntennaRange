$(document).ready(function() {
    $(function() {
        $("#navbar").load("../NavBar/nav.html", function() {
            $("#Models").addClass("navButton active").removeClass("navButton");
        });
    })
})