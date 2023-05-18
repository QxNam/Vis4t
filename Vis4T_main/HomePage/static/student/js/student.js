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

var subject_list = JSON.parse($('#subject-json').text());
function renderStudentDetailBarChart(data) {
          var subject_score = data;
          const chartData = subject_score.map(entry => ({
              x: entry["subject__subject_name"],
              y: entry.score_10,
          }));
          
          const options = {
              series: [{
                  name: "Điểm theo thang 10",
                  data: chartData
              }],
              chart: {
                  height: 400,
                  type: "bar",
                  toolbar: {
                  show: !0,
                  },
              },
              plotOptions: {
                  bar: {
                      horizontal: false,
                      columnWidth: "30%",
                      borderRadius: 3,
                  }
              },
              title:{
              text: "ĐIỂM TRUNG BÌNH MÔN HỌC",
              align: 'center',
              style: {
                  fontSize:  '25px',
                  fontFamily: 'fangsong',
              }
              },
              xaxis: {
              title: {
                  floating: true,
                  style: {
                      fontSize: "20px",
                      fontFamily: "fangsong",
                  },
              },
              tickAmount: 15,
              labels: {
                  offsetX: 0,
                  offsetY: 0,
              },
              },
              yaxis: {
              max: 10,
                  title: {
                      floating: true,
                      style: {
                          fontSize: "15px",
                          fontFamily: "fangsong",
                      },
                  },
                  labels: {
                      align: "center",
                      tickAmount: 6,
                      max: 10,
                  },
              },
              colors: ["#00E396"],
              dataLabels: {
                  enabled: false,
                  style:{
                  colors: ['#2196F3']
                  }
              },
              responsive: [
              {
                  breakpoint: 480,
                  options: {
                      chart: {
                          width: 300,
                          height: 300,
                      },
                      legend: {
                          position: "bottom",
                          show: !1,
                      },
                  },
              },
          ]
          };
          const chart = new ApexCharts(
              document.querySelector(".my-bar-chart-student"),
              options
          );
          chart.render();
}
drawCreditRadialChart();
renderStudentDetailBarChart(subject_list);

$('.dropdown-class').click(function(){
  var id = $(this).attr('data-student-id');
  window.location.href = '/student/' + id;
});

var table2 = new Tabulator("#table-student-object-score", {
  data: subject_list,
  layout:"fitColumns",
  tooltips:true, 
  columns:[
  {title: "Môn học", field: "subject__subject_name",},
  {title: "Điểm", field: "score_10",width: 80,hozAlign:"center"},
  {title: "Số tín chỉ", field: "subject__credit", sorter:"number", width: 120,hozAlign:"center"},
  ]

});