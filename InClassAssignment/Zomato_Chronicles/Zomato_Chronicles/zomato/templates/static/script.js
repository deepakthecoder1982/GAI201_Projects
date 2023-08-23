// Add this script to a file named script.js and place it in your static folder

document.querySelectorAll('.edit-button').forEach(button => {
    button.addEventListener('click', function() {
        const form = this.parentElement.querySelector('.add-dish-form');
        form.style.display = form.style.display === 'none' ? 'block' : 'none';
    });
});
