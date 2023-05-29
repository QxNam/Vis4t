$(document).ready(function() {
  $('.note-class-confirm').on('click', function() {
    var tag = $('textarea[name="message-un-id"]');
    var note = tag.val().trim();
    if (note.length == 0) {
      alert("Không thể thêm ghi chú rỗng. Thầy/cô vui lòng thêm ghi chú trước khi xác nhận");
      return false;
    }
    var date = $('p[name="title-un-id"]').data('date');
    
  });
});