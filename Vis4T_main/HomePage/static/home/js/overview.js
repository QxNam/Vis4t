function is_checked() {
  return $('#flexSwitchCheckDefault').is(':checked');
}
function render_pie_chart(class_name, score_text = 'ĐIỂM CHỮ') {
  fetch(get_class_url(class_name))
  .then(response => response.json())
  .then(data => {
    const ctx = document.getElementById('myClassChart');
    const LABELS = {'A+': '#257a24', 'A': '#3C8321', 'B': '#5A8C1E', 
                    'B+': '#7E951A', 'C': '#9E9315', 'C+': '#A38413', 
                    'D': '#AC600D', 'D+': '#B53307', 'F': '#BF0303'}; // Array of labels
    var { class_info, student, score_char_data, rank_data } = data.data;
    if (score_text == 'HỌC LỰC') {
      rendered_data = rank_data;
    }
    else {
      rendered_data = score_char_data;
    }
    var chart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: Object.keys(rendered_data),
        datasets: [{
          data: Object.values(rendered_data),
          borderWidth: 1,
          backgroundColor: Object.values(LABELS)
        }]
      },
      options: {
        plugins: {
          legend: {
            display: true,
            position: 'top',
            labels: {
              color: 'green'  
            }
          },
          title: {
            display: true,
            text: `BIỂU ĐỒ THỐNG KÊ ${score_text} CỦA LỚP ` + class_name,
            fontSize: 30
          }
        }
      }
    });
  })
}

function renderCSVTable(class_name){
  fetch(get_class_url(class_name))
  .then(response => response.json())
  .then(data => {
      var tabledata = []
      var { class_info, student, score_char_data, rank_data } = data.data;
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
    $("canvas").remove();
    $(".pie-chart").append('<canvas id="myClassChart" width="400" height="400"></canvas>');
    renderCSVTable(class_name);
    is_check = is_checked();
    if (!is_check) {
      render_pie_chart(class_name);
    }
    else {
      render_pie_chart(class_name, 'HỌC LỰC');
    }
});

document.addEventListener("DOMContentLoaded", function() {
    var class_name = document.getElementById("class-name").innerHTML;
    renderCSVTable(class_name);
    render_pie_chart(class_name)
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
      $("canvas").remove();
      $(".pie-chart").append('<canvas id="myClassChart" width="400" height="400"></canvas>');
      var class_name = $('#class-name').text();
      render_pie_chart(class_name, score_text);
  })