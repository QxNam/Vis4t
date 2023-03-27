function renderCSVTable(class_name){
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
                {title: "Mã số", field: "Mã số", width: 80},
                {title: "Họ tên", field: "Họ tên", width: 155},
                {title: "Điểm 10", field: "Điểm 10", sorter:"number", align:"right", width: 90},
                {title: "Điểm 4", field: "Điểm 4", width: 90},
                {title: "Điểm chữ", field: "Điểm chữ", width: 100},
                {title: "Xếp hạng", field: "Xếp hạng", width: 120},
                {title: "Số tín chỉ", field: "Số tín chỉ đã học xong", width: 100},
            ]  
        });

        
    });
}


$(".dropdown-class").on("click", function() {
    class_name = this.id.split(" ")[0];
    renderCSVTable(class_name);
});

document.addEventListener("DOMContentLoaded", function() {
    var class_name = document.getElementById("class-name").innerHTML;
    renderCSVTable(class_name);
});

const ctx = document.getElementById('myClassChart');
new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});