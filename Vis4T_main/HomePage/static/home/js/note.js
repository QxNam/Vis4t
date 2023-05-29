// 'use strict';
// console.log($('link[href="/static/home/css/note.css"]').data('add-note-url'));
$(document).ready(function() {
  $('.note-class-confirm').on('click', function() {
    var tag = $('textarea[name="message-un-id"]');
    var note = tag.val().trim();
    if (note.length == 0) {
      alert("Không thể thêm ghi chú rỗng. Thầy/cô vui lòng thêm ghi chú trước khi xác nhận");
      return false;
    }
    var token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
      url: '/add_note_class/',
      type : "POST",
      data: {
        'note': note,
        'csrfmiddlewaretoken': token
      },
      success: function(data) {
        
        if (data['status'] == 'success') {
          alert("Thêm ghi chú thành công");
          tag.val('');
          // refresh page
          location.reload();
        }
        else {
          alert("Lỗi! Thêm ghi chú thất bại");
        }
      }
    });    
  });

  $('.delete-class-note').on('click', function() {
    var note_id = $(this).data('note-id');
    var token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
      url: `/delete_note_class/${note_id}`,
      type : "DELETE",
      dataType: "json",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        'X-CSRFToken': token
      },
      success: function(data) {
          
          if (data['status'] == 'success') {
            alert("Xóa ghi chú thành công");
            location.reload();
          }
          else {
            alert("Lỗi! Xóa ghi chú thất bại");
          }
        }
      });

  });

  $('#save-class-note').on('click', function() {
    var note_id = $(this).data('note-id');
    var token = $('input[name=csrfmiddlewaretoken]').val();
    var name = `note-id-${note_id}`;
    $.ajax({
      url: `/update_note_class/${note_id}`,
      type : "PUT",
      dataType: "json",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        'X-CSRFToken': token
      },
      data: {
        'note': $("textarea[name="+ name + "]").val().trim(),
      },
      success: function(data) {
          
          if (data['status'] == 'success') {
            alert("Cập ghi chú thành công");
            location.reload();
          }
          else {
            alert("Lỗi! Xóa ghi chú thất bại");
          }
        }
      });

  });

});

