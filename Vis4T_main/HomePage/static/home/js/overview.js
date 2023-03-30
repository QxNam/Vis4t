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
              {title: "Xếp hạng", field: "Xếp hạng", width: 120},
              {title: "Số tín chỉ", field: "Số tín chỉ đã học xong", width: 100},
          ]  
      });

      const ctx = document.getElementById('myClassChart');
      const LABELS = {'A+': '#257a24', 'A': '#3C8321', 'B': '#5A8C1E', 
                      'B+': '#7E951A', 'C': '#9E9315', 'C+': '#A38413', 
                      'D': '#AC600D', 'D+': '#B53307', 'F': '#BF0303'}; // Array of labels
      console.log(score_char_data);
      var chart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: Object.keys(score_char_data),
          datasets: [{
            data: Object.values(score_char_data),
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
            }
          }
        }
      });
  });
}

$(".dropdown-class").on("click", function() {
    class_name = this.id.split(" ")[0];
    $("canvas").remove();
    $(".pie-chart").append('<canvas id="myClassChart" width="400" height="400"></canvas>');
    renderCSVTable(class_name);
});

document.addEventListener("DOMContentLoaded", function() {
    var class_name = document.getElementById("class-name").innerHTML;
    renderCSVTable(class_name);
});

