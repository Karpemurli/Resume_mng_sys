{% extends 'dashboard/header_footer.html' %}
{% load static %}
{% load widget_tweaks %}

{% block title %}Edit Profile{% endblock %}

{% block content %}
<div class="content-wrapper">
    <div class="row">
        <div class="col-md-8 offset-md-2 grid-margin stretch-card">
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Edit Profile</h4>
                    <p class="card-description">Update your personal information</p>

                    <!-- Messages/Alerts -->
                    {% if messages %}
                        {% for message in messages %}
                        <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                            {{ message }}
                            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                        {% endfor %}
                    {% endif %}

                    <!-- Edit Form -->
                    <form method="POST" class="forms-sample" id="profileForm">
                        {% csrf_token %}

                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label>Username</label>
                                    {% render_field form.username class="form-control" placeholder="Username" %}
                                    {% if form.username.errors %}
                                        <small class="text-danger">{{ form.username.errors.0 }}</small>
                                    {% endif %}
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label>Email</label>
                                    {% render_field form.email class="form-control" placeholder="Email" %}
                                    {% if form.email.errors %}
                                        <small class="text-danger">{{ form.email.errors.0 }}</small>
                                    {% endif %}
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label>First Name</label>
                                    {% render_field form.first_name class="form-control" placeholder="First Name" %}
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label>Last Name</label>
                                    {% render_field form.last_name class="form-control" placeholder="Last Name" %}
                                </div>
                            </div>
                        </div>

                        <div class="row">
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label>Phone</label>
                                    {% render_field form.phone class="form-control" placeholder="Phone" id="phoneInput" %}
                                    <small class="text-muted">Format: 1234567890 or 123-456-7890</small>
                                    <div id="phoneError" class="invalid-feedback" style="display:none;"></div>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="form-group">
                                    <label>Gender</label>
                                    {% render_field form.gender class="form-control" %}
                                </div>
                            </div>
                        </div>

                        <div class="form-group">
                            <label>Address</label>
                            {% render_field form.address class="form-control" placeholder="Street Address" rows="2" %}
                        </div>

                        <div class="row">
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label>Country</label>
                                    {% render_field form.country class="form-control" %}
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label>State</label>
                                    {% render_field form.state class="form-control" %}
                                </div>
                            </div>
                            <div class="col-md-4">
                                <div class="form-group">
                                    <label>City</label>
                                    {% render_field form.city class="form-control" %}
                                </div>
                            </div>
                        </div>

                        <div class="d-flex justify-content-between mt-4">
                            <button type="submit" class="btn btn-primary me-2" id="submitBtn">
                                <i class="mdi mdi-content-save"></i> Update Profile
                            </button>
                            <button type="button" class="btn btn-light" id="resetBtn">
                                <i class="mdi mdi-refresh"></i> Reset Form
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

{% block scripts %}
<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Sound effect from SoundJay
        const clickSound = new Audio("https://www.soundjay.com/buttons/sounds/button-20.mp3");

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
</script>
{% endblock %}

{% endblock %}