document.addEventListener("DOMContentLoaded", function () {
    const phoneInput = document.getElementById("phoneInput");
    const phoneError = document.getElementById("phoneError");
    const form = document.getElementById("profileForm");
    const resetButton = document.getElementById("resetButton");

    // Allow only numbers in phone input
    phoneInput.addEventListener("input", () => {
        phoneInput.value = phoneInput.value.replace(/\D/g, "").slice(0, 10);
    });

    // Validate Phone Number on Submit
    form.addEventListener("submit", function (e) {
        const phone = phoneInput.value.trim();
        const phonePattern = /^\d{10}$/;

        if (!phonePattern.test(phone)) {
            phoneInput.classList.add("is-invalid");
            phoneError.classList.remove("d-none");
            e.preventDefault();
        } else {
            phoneInput.classList.remove("is-invalid");
            phoneError.classList.add("d-none");
        }
    });

    // Reset button logic
    resetButton.addEventListener("click", function (e) {
        e.preventDefault();
        const fields = form.querySelectorAll("input, textarea, select");
        fields.forEach(field => {
            if (!["hidden", "submit", "reset"].includes(field.type)) {
                if (field.tagName === "SELECT") {
                    field.selectedIndex = 0;
                } else {
                    field.value = "";
                }
            }
        });

        // Remove validation
        document.querySelectorAll(".is-invalid").forEach(el => el.classList.remove("is-invalid"));
        document.querySelectorAll(".invalid-feedback").forEach(el => el.classList.add("d-none"));
    });

    // Sound on focus
    const sound = new Audio("https://www.soundjay.com/buttons/sounds/button-20.mp3");
    const focusFields = document.querySelectorAll("input, textarea, select");

    focusFields.forEach(field => {
        field.addEventListener("focus", () => {
            sound.currentTime = 0;
            sound.play().catch(err => {
                console.warn("Autoplay blocked:", err);
            });
        });
    });
});
