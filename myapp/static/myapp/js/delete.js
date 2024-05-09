// delete_form.js
document.addEventListener('DOMContentLoaded', function() {
    const deleteForm = document.getElementById('deleteForm');
    deleteForm.addEventListener('submit', function(event) {
       event.preventDefault();
        const url = this.action;
        const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

        axios.delete(url, {
            headers: {
                'X-CSRFToken': csrfToken
            }
        })
        .then(response => {
            alert('Person deleted successfully');
            window.location.reload();  // Reload the page or redirect as needed
        })
        .catch(error => {
            console.error('Error deleting person:', error);
            alert('Error deleting person');
        });
    });
});