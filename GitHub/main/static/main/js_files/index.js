const element_btn = document.querySelector('.btn-plus');
const element_title = document.querySelector('.title')

element_btn.addEventListener('click', () => {
    window.location.href = '/addrepo/';
})

element_title.addEventListener('click', () => {
    window.location.href = '/';
})

