const btn_addTask = document.querySelector('.btn-add')
const div_container_with_button = document.querySelector('#container-add-btn')

btn_addTask.addEventListener('click', () => {
    if(div_container_with_button.className == "work-add-task") {
        div_container_with_button.className = "hidden-add-task";
    } else {
        div_container_with_button.className = "work-add-task"
    }
    
})


document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
    cb.addEventListener('change', function () {
        const id = this.dataset.id;
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        fetch(`/toggle/${id}/`, {
            method: 'POST',
            headers: { 'X-CSRFToken': csrfToken }
        });
        const total = document.querySelectorAll('input[type="checkbox"]').length
    const completed = document.querySelectorAll('input[type="checkbox"]:checked').length
    document.getElementById("task-counter").textContent = `${completed} / ${total}`
    });
    
    
});
