var tabledata = []

var student_jsondata = JSON.parse($('#student-json').text());
var student = student_jsondata;
for (var i = 0; i < student.length; i++) {
    tabledata.push({
        "Mã số": student[i].student_id,
        "Họ tên": student[i].student_name,
        "Điểm 10": student[i].score_10,
        "Điểm 4": student[i].score_4,
        "Điểm chữ": student[i].score_char,
        "Xếp hạng": student[i].rank,
        "Số tín chỉ đã học xong": student[i].passed_credit,
        "Đã tốt nghiệp": student[i].is_graduated,
    })
}
var table = new Tabulator(".csv-table", {
    placeholder:"Chưa có lớp",
    data: tabledata,
    layout:"fitColumns",

    tooltips:true, 
    columns: [{
        title: "BẢNG KẾT QUẢ HỌC TẬP",
        columns:[
        {title: "Mã số", field: "Mã số",hozAlign:"center"},
        {title: "Họ tên", field: "Họ tên",width : 200},
        {title: "Điểm 10", field: "Điểm 10", sorter:"number",hozAlign:"center"},
        {title: "Điểm 4", field: "Điểm 4",hozAlign:"center"},
        {title: "Điểm chữ", field: "Điểm chữ",hozAlign:"center"},
        {title: "Học lực", field: "Xếp hạng",hozAlign:"center"},
        {title: "Số tín chỉ", field: "Số tín chỉ đã học xong",hozAlign:"center"},
        {title: "Tốt nghiệp", field: "Đã tốt nghiệp", hozAlign:"center", formatter:"tickCross", sorter:"boolean", editor:false},
        ]
    }],
  
});

table.on("cellClick", function(e, cell){
  var student_id = cell.getRow().getData()['Mã số'];
  console.log(student_id);
  window.location.href = '/student/' + student_id;
});


$(document).ready(function() {
  $.ajax({
    url: get_class_url(),
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      render_pie_chart(data);
      render_bar_chart(data, class_name);
      render_hist_chart(data, class_name);
      // render_box_plot(data, class_name);

    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
});








