$(".dropdown-class").on("click", function() {
    class_name = this.id.split(" ")[0];
    fetch(get_class_url(class_name))
    .then(response => response.json())
    .then(data => {
        var { class_info, student } = data.data;
        
    });
});