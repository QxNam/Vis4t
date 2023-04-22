
document.addEventListener("DOMContentLoaded", function() {
    renderCSVTable(class_name);
    fetch(get_class_url(class_name))
    .then(response => response.json())
    .then(data => {
      render_pie_chart(data);
      render_bar_chart(data, class_name);
    });
});