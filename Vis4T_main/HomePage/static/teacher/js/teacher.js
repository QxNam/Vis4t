$("a.undergraduate").click(function(){
    var numberOfStudent = $(this).data("class-number-of-student");
    var classMajor = $(this).data("class-major");
    var totalCredit = $(this).data("total-credit");
    
    $("span.undergraduate.name").text($(this).text());
    $("span.undergraduate.student-number").text(numberOfStudent);
    $("span.undergraduate.major").text(classMajor);
    $("span.undergraduate.credit").text(totalCredit);
  });