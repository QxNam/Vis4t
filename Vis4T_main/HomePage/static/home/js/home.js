$(".dropdown-item").on("click", function() {
    var [name_class, number] = this.id.split(" ");
    $("#class-name").html(name_class);
    $("#current-class-number").html(number);
    $("#dropdownMenuButton").html(name_class);
});

var chartPos = $(".chart").offset().left;
$(".arrow").css("left", $(".overall-btn").offset().left - chartPos + $(".overall-btn").width() / 2 - 7 + "px");
$(".option-1").click(function () {
    $(".option-1").removeClass("active");
    $(this).addClass("active");

    feature_id = $(this).attr("id");
    $(".feature").removeClass("atv");
    $("." + feature_id).addClass("atv");
    
    $(".arrow").css("left", $(this).offset().left - chartPos + $(this).width() / 2 - 7 + "px");

    setTimeout(() => {
        window.scrollTo({
        top: 99999,
        behavior: 'smooth',
    })},0);
}); 


