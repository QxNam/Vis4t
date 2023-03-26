$(".dropdown-class").on("click", function() {
    class_name = this.id.split(" ")[0];
    fetch(get_class_url(class_name))
    .then(response => response.json())
    .then(data => {
        var tabledata = []
        var { class_info, student } = data.data;
        for (var i = 0; i < student.length; i++) {
            tabledata.push({
                "Mã số": student[i].student_id,
                "Họ tên": student[i].student_name,
                "Điểm 10": student[i].score_10,
                "Điểm 4": student[i].score_4,
                "Điểm chữ": student[i].score_char,
                "Xếp hạng": student[i].rank,
                "Số tín chỉ đã học xong": student[i].passed_credit
            })
        }
        var table = new Tabulator(".csv-table", {
            placeholder:"Chưa có lớp",
            data: tabledata,
            layout:"fitColumns",
            tooltips:true,
            columns: [
                {title: "Mã số", field: "Mã số", width: 150},
                {title: "Họ tên", field: "Họ tên", width: 150},
                {title: "Điểm 10", field: "Điểm 10", sorter:"number", align:"right", width: 50},
                {title: "Điểm 4", field: "Điểm 4", width: 50},
                {title: "Điểm chữ", field: "Điểm chữ", width: 50},
                {title: "Xếp hạng", field: "Xếp hạng", width: 60},
                {title: "Số tín chỉ đã học xong", field: "Số tín chỉ đã học xong", width: 150},
            ]  
        });

        
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var class_name = document.getElementById("class-name").innerHTML;
    fetch(get_class_url(class_name))
    .then(response => response.json())
    .then(data => {
        var tabledata = []
        var { class_info, student } = data.data;
        for (var i = 0; i < student.length; i++) {
            tabledata.push({
                "Mã số": student[i].student_id,
                "Họ tên": student[i].student_name,
                "Điểm 10": student[i].score_10,
                "Điểm 4": student[i].score_4,
                "Điểm chữ": student[i].score_char,
                "Xếp hạng": student[i].rank,
                "Số tín chỉ đã học xong": student[i].passed_credit
            })
        }
        var table = new Tabulator(".csv-table", {
            placeholder:"Chưa có lớp",
            data: tabledata,
            layout:"fitColumns",
            tooltips:true,  
            columns: [
                {title: "Mã số", field: "Mã số", width: 150},
                {title: "Họ tên", field: "Họ tên", width: 150},
                {title: "Điểm 10", field: "Điểm 10", sorter:"number", align:"right", width: 50},
                {title: "Điểm 4", field: "Điểm 4", width: 50},
                {title: "Điểm chữ", field: "Điểm chữ", width: 50},
                {title: "Xếp hạng", field: "Xếp hạng", width: 60},
                {title: "Số tín chỉ đã học xong", field: "Số tín chỉ đã học xong", width: 150}
            ]  
        });

        
        
    });
});
// var tabledata = [
//     {id:1, name:"Billy Bob", age:12, gender:"male", height:95, col:"red", dob:"14/05/2010"},
//     {id:2, name:"Jenny Jane", age:42, gender:"female", height:142, col:"blue", dob:"30/07/1954"},
//     {id:3, name:"Steve McAlistaire", age:35, gender:"male", height:176, col:"green", dob:"04/11/1982"},
// ];

// //define table
// var table = new Tabulator(".csv-tabe", {
// });