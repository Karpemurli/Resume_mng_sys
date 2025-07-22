
    document.addEventListener('DOMContentLoaded', function() {
        // Sound effect from SoundJay
        const clickSound = new Audio("https://www.soundjay.com/buttons/sounds/button-30.mp3");

        // Play sound function with error handling
        function playClickSound() {
            try {
                clickSound.currentTime = 0; // Reset sound to start
                clickSound.volume = 0.3; // Lower volume
                clickSound.play().catch(e => console.log("Sound playback prevented:", e));
            } catch (e) {
                console.log("Sound error:", e);
            }
        }

        // Add click sound to all interactive elements
        document.querySelectorAll('input, select, textarea, button').forEach(element => {
            element.addEventListener('focus', playClickSound);
            element.addEventListener('click', playClickSound);
        });

        // Phone number validation
        const phoneInput = document.getElementById('phoneInput');
        const phoneError = document.getElementById('phoneError');

        function validatePhoneNumber(phone) {
            // Regular expression for phone numbers (10 digits with optional hyphens)
            const regex = /^(\d{3}-?\d{3}-?\d{4}|\d{10})$/;
            return regex.test(phone);
        }

        phoneInput.addEventListener('input', function() {
            if (phoneInput.value && !validatePhoneNumber(phoneInput.value)) {
                phoneInput.classList.add('is-invalid');
                phoneError.textContent = 'Please enter a valid phone number (10 digits, hyphens optional)';
                phoneError.style.display = 'block';
            } else {
                phoneInput.classList.remove('is-invalid');
                phoneError.style.display = 'none';
            }
        });

        // Enhanced reset functionality
        const form = document.getElementById('profileForm');
        const resetBtn = document.getElementById('resetBtn');

        resetBtn.addEventListener('click', function() {
            playClickSound();
            if (confirm('Are you sure you want to reset all changes?')) {
                form.reset();
                // Clear validation errors
                document.querySelectorAll('.is-invalid').forEach(el => {
                    el.classList.remove('is-invalid');
                });
                phoneError.style.display = 'none';
            }
        });

        // Form submission validation
        form.addEventListener('submit', function(event) {
            // Validate phone number before submission
            if (phoneInput.value && !validatePhoneNumber(phoneInput.value)) {
                event.preventDefault();
                phoneInput.classList.add('is-invalid');
                phoneError.textContent = 'Please enter a valid phone number before submitting';
                phoneError.style.display = 'block';
                phoneInput.focus();
                playClickSound();
            }
        });
    });
