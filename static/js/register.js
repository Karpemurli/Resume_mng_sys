
// Enhanced form validation with sound effects, reset, auto-focus and phone validation
document.addEventListener('DOMContentLoaded', function() {
  // Sound effect configuration
  const soundEnabled = true;
  const clickSound = new Audio("https://www.soundjay.com/buttons/sounds/button-20.mp3");
  const errorSound = new Audio("https://www.soundjay.com/buttons/sounds/button-20.mp3");
  clickSound.volume = 0.3;
  errorSound.volume = 0.3;

  // Form reference
  const form = document.getElementById('registrationForm');
  if (!form) return;

  // Auto-focus on First Name field when page loads
  const firstNameField = document.getElementById('id_first_name');
  if (firstNameField) {
    firstNameField.focus();
  }

  // Phone number field reference
  const phoneField = document.getElementById('id_phone');

  // Prevent non-numeric input in phone field
  if (phoneField) {
    phoneField.addEventListener('input', function() {
      this.value = this.value.replace(/\D/g, ''); // Remove non-digits
      if (this.value.length > 10) {
        this.value = this.value.slice(0, 10); // Limit to 10 digits
      }
    });
  }

  // Reset form function
  function resetForm() {
    form.reset();
    form.classList.remove('was-validated');

    // Clear all validation states
    form.querySelectorAll('input, select, textarea').forEach(field => {
      field.classList.remove('is-invalid', 'touched');
    });

    // Re-focus on First Name field after reset
    if (firstNameField) {
      firstNameField.focus();
    }

    // Play sound if enabled
    if (soundEnabled) {
      clickSound.currentTime = 0;
      clickSound.play().catch(e => console.log("Sound blocked:", e));
    }
  }

  // Add reset button event
  const resetBtn = form.querySelector('button[type="reset"]');
  if (resetBtn) {
    resetBtn.addEventListener('click', resetForm);
  }

  // Sound effect for form interactions with debouncing
  let lastSoundTime = 0;
  const soundDebounceTime = 300; // milliseconds

  form.querySelectorAll('input, select').forEach(field => {
    field.addEventListener("focus", function() {
      if (!soundEnabled) return;

      const now = Date.now();
      if (now - lastSoundTime > soundDebounceTime) {
        clickSound.currentTime = 0;
        clickSound.play().catch(e => console.log("Sound blocked:", e));
        lastSoundTime = now;
      }
    });
  });

  // Custom validation for phone number (10 digits)
  function validatePhoneNumber(field) {
    const phoneValue = field.value.trim();
    const phoneRegex = /^\d{10}$/;

    if (!phoneRegex.test(phoneValue)) {
      field.classList.add('is-invalid');
      field.nextElementSibling.textContent = field.dataset.errorPattern || 'Please enter a valid 10-digit phone number';
      return false;
    }
    field.classList.remove('is-invalid');
    return true;
  }

  // Field validation function
  function validateField(field) {
    // Special handling for phone number field
    if (field.id === 'id_phone' || field.name === 'phone') {
      return validatePhoneNumber(field);
    }

    // Standard validation for other fields
    if (!field.checkValidity()) {
      field.classList.add('is-invalid');

      if (field.validity.valueMissing) {
        field.nextElementSibling.textContent = field.dataset.errorRequired || 'This field is required';
      } else if (field.validity.typeMismatch) {
        field.nextElementSibling.textContent = field.dataset.errorType || 'Invalid format';
      }

      return false;
    } else {
      field.classList.remove('is-invalid');
      return true;
    }
  }

  // Add validation on blur with debounce
  let validationTimer;
  form.querySelectorAll('input, select').forEach(input => {
    input.addEventListener('blur', function() {
      clearTimeout(validationTimer);
      validationTimer = setTimeout(() => {
        this.classList.add('touched');
        validateField(this);
      }, 200);
    });

    // Real-time validation for specific fields
    if (input.type === 'email' || input.type === 'password' ||
        input.id === 'id_phone' || input.name === 'phone') {
      input.addEventListener('input', function() {
        if (this.classList.contains('touched')) {
          validateField(this);
        }
      });
    }
  });

  // Form submission handler
  form.addEventListener('submit', function(event) {
    let isValid = true;
    const submitBtn = form.querySelector('[type="submit"]');
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Processing...';

    // Play submit sound if enabled
    if (soundEnabled) {
      clickSound.currentTime = 0;
      clickSound.play().catch(e => console.log("Sound blocked:", e));
    }

    // Validate all fields
    form.querySelectorAll('input, select').forEach(input => {
      input.classList.add('touched');
      if (!validateField(input)) {
        if (isValid) {
          input.focus(); // Focus first invalid field
        }
        isValid = false;
      }
    });

    if (!isValid) {
      event.preventDefault();
      event.stopPropagation();
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalBtnText;

      // Play error sound if enabled
      if (soundEnabled) {
        errorSound.currentTime = 0;
        errorSound.play().catch(e => console.log("Sound blocked:", e));
      }
    }

    form.classList.add('was-validated');
  });
});
