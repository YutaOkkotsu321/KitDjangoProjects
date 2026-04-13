const btn_addTask = document.querySelector('.btn-add')
const div_container_with_button = document.querySelector('#container-add-btn')
btn_addTask.addEventListener('click', () => {
    if(div_container_with_button.className == "work-add-task") {
        div_container_with_button.className = "hidden-add-task";
    } else {
        div_container_with_button.className = "work-add-task"
    }
    
})