

function drawCreditRadialChart(student_credits, total_credits) {
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
        $('.student-credit').empty();
        var chart = new ApexCharts(document.querySelector(".student-credit"), options);
        chart.render();
      }
      

    function displayStudentDataOnIndex(student_index){
        student_data = student_jsondata[student_index];
        $('.dropdownStudent .btn span').text(student_data.student_name);
        $('.name-student h2').text(student_data.student_name);
        $('.student-score10 div').text(student_data.score_10);
        $('.student-score4 div').text(student_data.score_4);
        $('.student-scorechar').text(student_data.score_char);
        $('.student-rank').text(student_data.rank);
        $('.student-id span').text(" " + student_data.student_id);
        $('.student-active span').text(" " + student_data.is_active ? 'Đã tốt nghiệp' : 'Chưa tốt nghiệp');
        $('.student-gmail span').text(" " + student_data.student_gmail);

        
        drawCreditRadialChart(student_data.passed_credit);
        renderStudentDetailBarChart(student_data.student_id);
    }
    let student_jsondata = JSON.parse($('#student-json').text());
    
    
    $('.dropdown-class').click(function(){
        let index = $(this).data('student');
        displayStudentDataOnIndex(index);
    });

    drawCreditRadialChart(document.currentScript.dataset.studentCredit);