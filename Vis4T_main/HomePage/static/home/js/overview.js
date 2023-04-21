function is_checked() {
  return $('#flexSwitchCheckDefault').is(':checked');
}

function render_bar_chart(data){
    var { score10_data, score4_data } = data.data;
    rendered_data = score10_data;
    var options = {
      series: [{
        data: Object.values(rendered_data),
        type: "column",
    }, 
    {
      data: Object.values(rendered_data),
      type: "line",
    }],
      chart: {
        height: 350 ,
        type: "line",
        toolbar: {
            show: !0
        }
      },
      stroke: {
          width: [0, 3],
          curve: "smooth"
      },
      title:{
        text: 'Điểm sinh viên',
        align: 'center',
        style: {
          fontSize:  '25px',
          fontFamily: 'Roboto',
        }
      },
      plotOptions: {
          bar: {
              horizontal: !1,
              columnWidth: "20%"
          }
      },
      dataLabels: {
          enabled: !1
      },
      legend: {
          show: !1
      },
      
      colors: ["#6d77b9", "#5bceac"],
      labels: Object.keys(score10_data),

    };
    
    const chart = new ApexCharts(
        document.querySelector('#myBarChart'), 
        options
      )
    
    chart.render();
  }


function render_pie_chart(data, score_text = 'ĐIỂM CHỮ') {
    const LABELS = {'A+': '#68F600', 'A': '#6BDC18', 'B': '#78B13B', 
                    'B+': '#8FA238', 'C': '#E8E525', 'C+': '#E8C525', 
                    'D': '#E8A425', 'D+': '#E89225', 'F': '#EE310B'}; // Array of labels
    var { score_char_data, rank_data } = data.data;
    if (score_text == 'HỌC LỰC') {
      rendered_data = rank_data;
    }
    else {
      rendered_data = score_char_data;
    }
    var options = {
      series: Object.values(rendered_data),
      chart: {
        height: 200,
        type: 'pie'
      },
    labels: Object.keys(rendered_data),
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 300,
              height: 300
            },
            legend: {
              position: 'bottom'
            },
            
          }
        }]};
    
      const chart = new ApexCharts(
          document.querySelector('#myClassChart'), 
          options
        )
      
      chart.render();
        
  }

function renderCSVTable(class_name){
  fetch(get_class_detail_url(class_name))
  .then(response => response.json())
  .then(data => {
      var tabledata = []
      var student = data.student;
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
      new Tabulator(".csv-table", {
          placeholder:"Chưa có lớp",
          data: tabledata,
          layout:"fitColumns",

          tooltips:true,  
          columns: [
              {title: "Mã số", field: "Mã số", width: 80},
              {title: "Họ tên", field: "Họ tên", width: 155},
              {title: "Điểm 10", field: "Điểm 10", sorter:"number", align:"right", width: 90},
              {title: "Điểm 4", field: "Điểm 4", width: 90},
              {title: "Điểm chữ", field: "Điểm chữ", width: 100},
              {title: "Học lực", field: "Xếp hạng", width: 120},
              {title: "Số tín chỉ", field: "Số tín chỉ đã học xong", width: 100},
          ]  
      });

      
  });
}

document.addEventListener("DOMContentLoaded", function() {
    renderCSVTable(class_name);
    fetch(get_class_url(class_name))
    .then(response => response.json())
    .then(data => {
      console.log(data);
      render_pie_chart(data);
      render_bar_chart(data);
    });
    

});

let isCheckChangeChart = $('.btn-change-chart')
  isCheckChangeChart.click(function(){
      if(isCheckChangeChart.is(":checked")){
          $('.text_score').toggleClass('actBtn');
          $('.academic-rank').toggleClass('actBtn');
          score_text = "HỌC LỰC";
      }else{
          $('.text_score').toggleClass('actBtn');
          $('.academic-rank').toggleClass('actBtn');
          score_text = "ĐIỂM CHỮ";
      }
      $("#myClassChart").remove();
      $(".pie-chart").append('<div id="myClassChart"></div>');

      render_pie_chart(class_name, score_text);
      render_bar_chart(class_name);
});

