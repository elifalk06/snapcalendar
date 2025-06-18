// Provide simple client-side interactions
function showAddedMessage() {
    const msg = document.getElementById('added-msg');
    if (msg) {
        msg.style.display = 'block';
        setTimeout(() => msg.style.display = 'none', 2000);
    }
}

window.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', () => {
            showAddedMessage();
        });
    }
});
