const passwordEl = document.querySelector('.password')
const eyeEl = document.querySelector('.eye')
const unEyeEl = document.querySelector('.unEye')

eyeEl.onclick = (()=>{
    passwordEl.setAttribute('type','text')
    unEyeEl.classList.add('active')
    eyeEl.classList.remove('active')
})
unEyeEl.onclick = (()=>{
    passwordEl.setAttribute('type','password')
    unEyeEl.classList.remove('active')
    eyeEl.classList.add('active')
})

var count = 0;
$('.forgot-password').click(() => {

    $('.up-form').removeClass('flip-up');
    $('.back-form').removeClass('flip-down');

    $('.up-form').addClass('flip-down').hide();
    $('.back-form').show().addClass('flip-up');
  });
  
  $('.back-to-login').click(() => {
    $('.up-form').removeClass('flip-down');
    $('.back-form').removeClass('flip-up');
    
    $('.back-form').addClass('flip-down').hide();
    $('.up-form').show().addClass('flip-up');
});

$(document).ready(function() {
    $('#send-gmail').click(function(event) {
      event.preventDefault();
      var gmailValue = $('#gmail').val();
      $.ajax({
        url: '/gmail/',
        type: 'POST',
        data: {
          'gmail': gmailValue,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
          console.log(response);
        },
        error: function(xhr, status, error) {
          console.log(error);
        }
      });
    });
  });   