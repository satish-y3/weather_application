document.addEventListener('DOMContentLoaded', () => {
    const inputs = document.querySelectorAll('.input-box input, .input-box textarea');

    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.nextElementSibling.classList.add('focus');
        });

        input.addEventListener('blur', () => {
            if (input.value === '') {
                input.nextElementSibling.classList.remove('focus');
            }
        });
    });
});
