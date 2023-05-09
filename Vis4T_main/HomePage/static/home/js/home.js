var tabledata = []
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
  var student_index = student_jsondata.findIndex(function(student) {
    return student.student_id == student_id;
  });
  let chart_to_studentY = document.querySelector('.chart-to-student').offsetTop;
  console.log(chart_to_studentY);
  // tru 110 la do header co height 110px
  window.scrollTo(0,(chart_to_studentY - 110));
  displayStudentDataOnIndex(student_index);
});


$(document).ready(function() {
  $.ajax({
    url: get_class_url(),
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      render_pie_chart(data);
      render_bar_chart(data, class_name);
      render_box_plot(data, class_name);
      render_hist_chart(data, class_name);
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
});




const data_student_object = [
  {
    "subject__subject_name": "Toán cao cấp 1",
    "subject__subject_id": "2113431",
    "subject__credit": 2,
    "score_10": 9.9
  },
  {
    "subject__subject_name": "Lập trình hướng đối tượng",
    "subject__subject_id": "2101623",
    "subject__credit": 3,
    "score_10": 9.8
  },
  {
    "subject__subject_name": "Phát triển ứng dụng",
    "subject__subject_id": "2101657",
    "subject__credit": 3,
    "score_10": 9.7
  },
  {
    "subject__subject_name": "Nhập môn Lập trình",
    "subject__subject_id": "2101622",
    "subject__credit": 2,
    "score_10": 9.7
  },
  {
    "subject__subject_name": "Thống kê máy tính và ứng dụng",
    "subject__subject_id": "2101624",
    "subject__credit": 3,
    "score_10": 9.6
  },
  {
    "subject__subject_name": "Xác suất trong Khoa học Dữ liệu",
    "subject__subject_id": "2101676",
    "subject__credit": 2,
    "score_10": 9.6
  },
  {
    "subject__subject_name": "Tương tác người máy",
    "subject__subject_id": "2101428",
    "subject__credit": 3,
    "score_10": 9.5
  },
  {
    "subject__subject_name": "Logic học",
    "subject__subject_id": "2113438",
    "subject__credit": 3,
    "score_10": 9.5
  },
  {
    "subject__subject_name": "Logic học",
    "subject__subject_id": "2113438",
    "subject__credit": 3,
    "score_10": 9.5
  },
  {
    "subject__subject_name": "Logic học",
    "subject__subject_id": "2113438",
    "subject__credit": 3,
    "score_10": 9.5
  },
  {
    "subject__subject_name": "Logic học",
    "subject__subject_id": "2113438",
    "subject__credit": 3,
    "score_10": 9.5
  },
  {
    "subject__subject_name": "Logic học",
    "subject__subject_id": "2113438",
    "subject__credit": 3,
    "score_10": 9.5
  },
  {
    "subject__subject_name": "Logic học",
    "subject__subject_id": "2113438",
    "subject__credit": 3,
    "score_10": 9.5
  },
  {
    "subject__subject_name": "Logic học",
    "subject__subject_id": "2113438",
    "subject__credit": 3,
    "score_10": 9.5
  }
]




var table2 = new Tabulator("#table-student-object-score", {
  data: data_student_object,
  layout:"fitColumns",
  tooltips:true, 
  columns:[
  {title: "Môn học", field: "subject__subject_name",},
  {title: "Điểm", field: "score_10",width: 80,hozAlign:"center"},
  {title: "Số tín chỉ", field: "subject__credit", sorter:"number", width: 120,hozAlign:"center"},
  ]

});



