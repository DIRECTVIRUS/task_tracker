document.addEventListener('DOMContentLoaded', (event) => {
    // Add event listeners to edit buttons
    const editButtons = document.querySelectorAll('.edit-btn');
    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            const taskId = this.getAttribute('data-task-id');
            const title = this.getAttribute('data-task-title');
            const dueDate = this.getAttribute('data-task-due-date');
            const description = this.getAttribute('data-task-description');
            openEditModal(taskId, title, dueDate, description);
        });
    });
});

// Toggle description dropdown
function toggleDescription(button) {
    const description = button.nextElementSibling;
    description.classList.toggle('hidden');
    
    if (description.classList.contains('hidden')) {
        button.textContent = '▼ Show Description';
    } else {
        button.textContent = '▲ Hide Description';
    }
}

// Open edit modal
function openEditModal(taskId, title, dueDate, description) {
    const modal = document.getElementById('edit-modal');
    const editForm = document.getElementById('edit-form');
    
    document.getElementById('edit-title').value = title;
    document.getElementById('edit-due-date').value = dueDate;
    document.getElementById('edit-description').value = description;
    
    editForm.action = '/edit_task/' + taskId;
    modal.classList.remove('hidden');
}

// Close edit modal
function closeEditModal() {
    const modal = document.getElementById('edit-modal');
    modal.classList.add('hidden');
}

// Close modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById('edit-modal');
    if (event.target === modal) {
        modal.classList.add('hidden');
    }
}