
$(".dropdown-item").on("click", function() {
    var [name_class, number] = this.id.split(" ");
    $("#class-name").html(name_class);
    $("#current-class-number").html(number);
    $("#dropdownMenuButton").html(name_class);

    
});






