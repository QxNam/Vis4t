

function drawCreditRadialChart() {
    var student_credits = $('#student-script').data('student-credit');
    var total_credits = $('#student-script').data('class-total-credit');
    var percentage = (student_credits / total_credits) * 100;
    var options = {
      series: [100, percentage],
      chart: {
        height: 340,
        type: 'radialBar'
      },
      plotOptions: {
        radialBar: {
          dataLabels: {
            name: {
              fontSize: '22px'
            },
            value: {
                fontSize: '16px',
                formatter: function (val) {
                    return Math.round(val*total_credits/100);
                }
            },
            total: {
              show: true,
              label: 'Tổng số tín chỉ',
              formatter: function (_) {
                return total_credits;
              }
            }
          }
        }
      },
      labels: ['Tổng số tín chỉ', 'Tín chỉ đã học']
    };
    var chart = new ApexCharts(document.querySelector(".student-credit"), options);
    chart.render();
}

drawCreditRadialChart();

var subject_list = JSON.parse($('#subject-json').text());

function displayStudentDataOnIndex(student_index){
    
}

$('.dropdown-class').click(function(){
  var id = $(this).attr('data-student-id');
  window.location.href = '/student/' + id;
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