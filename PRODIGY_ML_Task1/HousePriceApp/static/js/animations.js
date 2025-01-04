document.addEventListener("DOMContentLoaded", function () {
    // Button hover effect
    const button = document.querySelector(".magic-button");
    button.addEventListener("mouseover", () => {
        button.style.transform = "scale(1.15)";
    });
    button.addEventListener("mouseout", () => {
        button.style.transform = "scale(1)";
    });

    // Form animation
    const form = document.querySelector(".animated-form");
    form.style.opacity = "0";
    form.style.transform = "translateY(-50px)";
    setTimeout(() => {
        form.style.transition = "all 1s ease";
        form.style.opacity = "1";
        form.style.transform = "translateY(0)";
    }, 500);
});
