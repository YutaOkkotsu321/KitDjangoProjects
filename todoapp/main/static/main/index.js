const btn_addTask = document.querySelector('.btn-add')
const div_container_with_button = document.querySelector('#container-add-btn')
const form = document.querySelector('#container-add-btn form')
btn_addTask.addEventListener('click', () => {
    if(div_container_with_button.className == "work-add-task") {
        div_container_with_button.className = "hidden-add-task";
    } else {
        div_container_with_button.className = "work-add-task"
    }
    
})

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form)
    fetch('', {
        method: "POST",
        body: formData,
        headers: {'X-CSRFToken': formData.get('csfrmiddlewaretoken')}
    }).then(() => {
        form.reset();
    })
})