function is_checked() {
  return $('#flexSwitchCheckDefault').is(':checked');
}

function render_bar_chart(class_name){
  fetch(get_class_url(class_name))
  .then(response => response.json())
  .then(data => {
    var { score10_data, score4_data } = data.data;
    rendered_data = score10_data;
    console.log(rendered_data);
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
        height: 300 ,
        type: "line",
        toolbar: {
            show: !0
        }
      },
      stroke: {
          width: [0, 3],
          curve: "smooth"
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
  })
}


function render_pie_chart(class_name, score_text = 'ĐIỂM CHỮ') {
  fetch(get_class_url(class_name))
  .then(response => response.json())
  .then(data => {
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
        width: 400,
        height: 300,  
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
        
  })
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

$(".dropdown-class").on("click", function() {
    class_name = this.id.split(" ")[0];
    $("#myClassChart").remove();
    $(".pie-chart").append('<div id="myClassChart"></div>');
    renderCSVTable(class_name);
    is_check = is_checked();
    if (!is_check) {
      render_pie_chart(class_name);
    }
    else {
      render_pie_chart(class_name, 'HỌC LỰC');
    }

    render_bar_chart(class_name);
    // Remove all content in div with class "bar-chart"
    $("#myBarChart").remove();
    $(".bar-chart").append('<div id="myBarChart"></div>');
});

document.addEventListener("DOMContentLoaded", function() {
    var class_name = document.getElementById("class-name").innerHTML;
    renderCSVTable(class_name);
    render_pie_chart(class_name);
    render_bar_chart(class_name);

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

      var class_name = $('#class-name').text();
      render_pie_chart(class_name, score_text);
      render_bar_chart(class_name);
})

