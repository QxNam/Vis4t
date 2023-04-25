$(document).ready(function() {
  renderCSVTable(class_name);
  $.ajax({
    url: get_class_url(class_name),
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      render_pie_chart(data);
      render_bar_chart(data, class_name);
      render_box_plot(data, class_name);
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log('Error:', errorThrown);
    }
  });
});