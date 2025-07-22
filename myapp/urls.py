from django.urls import path
from .views import *

urlpatterns = [
    # Main pages
    path('', home_view, name='home'),  # हे root URL आहे

    path('login/', loginView, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('index/', Index, name='index'),
    path('contact/', Contact, name='contact'),
    path('register/', register_view, name='register'),

    # Job listings
    path('jobs/', job_list, name='job_list'),
    path('jobs/<int:job_id>/apply/', apply_job, name='apply_job'),
    path('about/', about_view, name='about'),

    # Admin section
    path('admin-dashboard', admin_dashboard, name='admin_dashboard'),
    path('update-status/<int:application_id>/<str:status>/', update_status, name='update_status'),
    path('add-job/', add_job, name='add_job'),

    # User applications
    path('my-applications/', my_applications, name='my_applications'),

    # Dashboard and profile
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('registertable/', user_register_view, name='registertable'),
    path('update-register/', update_register, name='update_register'),
    path('dashboard/', user_dashboard, name='user-dashboard'),

    # Job management
    path('manage-jobs/', manage_jobs, name='manage_jobs'),
    path('edit-job/<int:job_id>/', edit_job, name='edit_job'),
    path('delete-job/<int:job_id>/', delete_job, name='delete_job'),
    path('jobs/<int:job_id>/', job_detail, name='job_detail'),

    # Messaging
    path('messages/', messages_list, name='messages_list'),

    # Application management
    path('delete-application/<int:app_id>/', delete_application, name='delete_application'),

    # Password change
    path('change-password/', password_change_request, name='change_password'),
    path('verify-password-otp/', verify_password_otp, name='verify_password_otp'),
    path('resend-otp/', resend_otp, name='resend_password_otp'),
]
