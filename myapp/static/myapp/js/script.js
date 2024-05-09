document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('RegistrationForm');
    const popup = document.getElementById('popup');
    const cancelBtn = document.getElementById('cancelBtn');
    const yesBtn = document.getElementById('yesBtn');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the default form submission
        const popup = document.getElementById('popup');
        popup.style.display = 'block';
    });

    cancelBtn.addEventListener('click', (event) => {
        event.preventDefault();
        if (confirm('Are you sure you want to cancel and discard changes?')) {
            hidePopup();
            form.reset();
        }
    });

    yesBtn.addEventListener('click', async (event) => {
        event.preventDefault();
        hidePopup();

        try {
            const formData = new FormData(form);
            const userData = {
                name: formData.get('name'),
                dob: formData.get('dob'),
                gen: formData.get('gen'),
                reg: formData.get('reg'),
                password:formData.get('password'),
            };

            const jsonString = JSON.stringify(userData);

            const response = await fetch('http://127.0.0.1:8000/mpapp/reg/', {
                method: 'POST',
                body: jsonString,
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
            });

            if (response.ok) {
                window.location.href = 'http://127.0.0.1:8000/mpapp/success/';
            } else {
                alert('Failed to save data. Please try again.');
            }
        } catch (error) {
            alert('An error occurred while processing the action.');
        }
    });

    function hidePopup() {
        popup.style.display = 'none';
    }

    function getCSRFToken() {
        const csrfTokenInput = document.querySelector('input[name=csrfmiddlewaretoken]');
        return csrfTokenInput ? csrfTokenInput.value : '';
    }
});
