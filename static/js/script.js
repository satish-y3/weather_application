function toggleNav() {
    const navLinks = document.querySelector('.nav-links');
    const isVisible = navLinks.style.display === 'flex';
    navLinks.style.display = isVisible ? 'none' : 'flex';
}
