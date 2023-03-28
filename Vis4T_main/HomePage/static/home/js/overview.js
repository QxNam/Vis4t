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
        var chart = new Chart(ctx, {
          type: 'pie',
          data: {
            labels: score_char_data[0],
            datasets: [{
              data: score_char_data[1],
              borderWidth: 1
            }]
          },
          options: {
            plugins: {
              legend: {
                  display: false,
                  labels: {
                      color: 'rgb(255, 99, 132)'
                  }
              }
            },
            scales: {
              y: {
                beginAtZero: true
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

