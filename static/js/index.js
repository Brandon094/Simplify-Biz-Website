document.addEventListener("DOMContentLoaded", function () {
    // Método para el menú hamburguesa
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

    // Obtener el año actual y agregarlo al documento (por ejemplo, en el pie de página)
    const yearElement = document.querySelector("#year"); // Asegúrate de tener un elemento con id="year" en el HTML
    const currentYear = new Date().getFullYear();
    if (yearElement) {
        yearElement.textContent = currentYear; // Establecer el año en el elemento
    }
});
console.log("El script se ha cargado correctamente");

