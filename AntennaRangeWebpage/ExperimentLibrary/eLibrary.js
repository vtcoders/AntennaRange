function toggle_filters() {
    filters = document.getElementById("filters");
    show_button = document.getElementById("show-filter-button")
    hide_button = document.getElementById("hide-filter-button")
    if (window.getComputedStyle(filters).display === "none") {
        filters.style.display = "block";
        show_button.style.display = "none";
        hide_button.style.display = "block";
    }
    else {
        filters.style.display = "none";
        show_button.style.display = "block";
        hide_button.style.display = "none";
    }
}

function uncheckAll() {
    $('input[type="checkbox"]:checked').prop('checked', false);
}