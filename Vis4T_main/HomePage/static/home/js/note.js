// 'use strict';
// console.log($('link[href="/static/home/css/note.css"]').data('add-note-url'));
var token = $('input[name=csrfmiddlewaretoken]').val();
$(document).ready(function() {
  $('.note-class-confirm').on('click', function() {
    var tag = $('textarea[name="message-un-id"]');
    var note = tag.val().trim();
    if (note.length == 0) {
      alert("Không thể thêm ghi chú rỗng. Thầy/cô vui lòng thêm ghi chú trước khi xác nhận");
      return false;
    }
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
    console.log(note_id);

    $.ajax({
      url: '/add_note_class/',
      type : "DELETE",
      data: {
        'note_id': note_id,
        'csrfmiddlewaretoken': token
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
});