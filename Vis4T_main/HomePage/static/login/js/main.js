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
