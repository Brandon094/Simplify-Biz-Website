//  Metodo para el menu hamburguesa
document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    // Alternar la visibilidad del menú
    menuToggle.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });

    // Ocultar el menú al hacer clic en un enlace (opcional)
    navLinks.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", function () {
            navLinks.classList.remove("active");
        });
    });
});

// Metodo pora cambiar el año del copyrigth
document.addEventListener("DOMContentLoaded", function () {
    const copyElement = document.getElementById("copy");
    const currentYear = new Date().getFullYear();
    copyElement.innerHTML = `&copy; ${currentYear} Simplify Biz. Todos los derechos reservados.`;
});
