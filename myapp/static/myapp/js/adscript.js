
document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript file loaded successfully.');
         const form = document.getElementById('addressForm');
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;


    // Event listener for form submission
    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent the default form submission
        // Show the popup after form submission
        console.log("*********in submit")
        // Show the popup after form submission
        const popup = document.getElementById('popup');
        popup.style.display = 'block';
    });

    // Function to handle cancel confirmation
   document.getElementById('cancelBtn').addEventListener('click', (event) => {
        event.preventDefault();
        if (confirm('Are you sure you want to cancel and discard changes?')) {
            // If user confirms cancel, hide the popup and reset form fields
            hidePopup();
            form.reset();// Reset form fields
            console.log("####in cancel")
        }
    });
        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('yesBtn').addEventListener('click', async (event) => {
                event.preventDefault();
                console.log('Button clicked!');

                const form = document.getElementById('addressForm');
                const csrfToken = 'csrf_token'; // Replace with your actual CSRF token

                try {
                    const formData = new FormData(form);
                    console.log(formData)
                    const userData = {
                        street: formData.get('street'),
                        city: formData.get('city'),
                        state: formData.get('state'),
                        zipcode: Number(formData.get('zipcode')),
                        person: Number(formData.get('person')),
                    };

                    const jsonString = JSON.stringify(userData);
                    console.log(jsonString)
                    const response = await fetch('http://127.0.0.1:8000/mpapp/address', {
                        method: 'POST',
                        body: jsonString,
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrfToken,
                        },
                    });
                    if (response.ok) {
                        window.location.href = 'http://127.0.0.1:8000/mpapp/success/';
                    } else {
                        alert('Failed to save data, try again!');
                    }
                } catch (error) {
                    console.error('An error occurred while processing the action:', error);
                    alert('An error occurred while processing the action.');
                }
            });
        });


    // Function to hide the popup
    function hidePopup() {
        const popup = document.getElementById('popup');
        popup.style.display = 'none';
    }
});
