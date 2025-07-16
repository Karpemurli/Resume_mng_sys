from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CandidateRegisterForm, ApplicationForm, JobForm, RegisterUpdateForm
from django.contrib import messages
from .models import Job, Application, CustomUser
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .signals import generate_otp
from .forms import ChangePasswordWithOTPForm
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
import random
import time
from django.utils.http import url_has_allowed_host_and_scheme




# Create your views here.

#  Register View
def register_view(request):
    if request.method == 'POST':
        form = CandidateRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.phone = form.cleaned_data['phone']
            user.gender = form.cleaned_data['gender']
            user.address = form.cleaned_data['address']
            user.country = form.cleaned_data['country']
            user.state = form.cleaned_data['state']
            user.city = form.cleaned_data['city']

            user.role = 'candidate'  # ✅ Corrected line

            user.save()

            # Send welcome email
            try:
                send_mail(
                    subject="Welcome to Resume Management System",
                    message=f"Hi {user.username},\n\nThank you for registering with us. You can now login and apply for jobs!",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")

            messages.success(request, "Registered successfully. You can now login.")
            return redirect('login')
    else:
        form = CandidateRegisterForm()

    return render(request, 'myapp/register.html', {'form': form})

@login_required
def user_register_view(request):
    user_data = request.user
    return render(request, 'dashboard/registertable.html', {'user_data': user_data})

#update
@login_required
def update_register(request):
    if request.user.is_staff:
        messages.error(request, "Admin is not allowed to edit the register profile.")
        return redirect('user-dashboard')  #  correct name now

    user = request.user

    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully.")
            return render(request, 'dashboard/update_register.html', {'form': form})
    else:
        form = RegisterUpdateForm(instance=user)

    return render(request, 'dashboard/update_register.html', {'form': form})




# Login View
def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Handle the 'next' parameter if it exists
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            # Otherwise redirect based on user role
            if user.is_staff or user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('job_list')  # Changed from 'job_list' to 'home'
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'myapp/login.html', {
        'next': request.GET.get('next', '')  # Pass the next parameter to template
    })


def logout_view(request):
    logout(request)
    return redirect('home')  # Always redirect to home page after logout


#  Home View
def home_view(request):
    total_candidates = CustomUser.objects.filter(role='candidate').count()
    total_jobs = Job.objects.count()
    total_filled_jobs = Application.objects.filter(status='Approved').count()
    total_companies = CustomUser.objects.filter(role='recruiter').count()

    job_titles = Job.objects.values_list('title', flat=True).distinct()
    locations = Job.objects.values_list('location', flat=True).distinct()
    job_types = Job.objects.values_list('job_type', flat=True).distinct()

    context = {
        'total_candidates': total_candidates,
        'total_jobs': total_jobs,
        'total_filled_jobs': total_filled_jobs,
        'total_companies': total_companies,
        'job_titles': job_titles,
        'locations': locations,
        'job_types': job_types,
    }

    return render(request, 'myapp/home.html', context)






@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'dashboard/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'dashboard/job_detail.html', {'job': job})


@login_required
def manage_jobs(request):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('job_list')

    jobs = Job.objects.all()
    return render(request, 'dashboard/manage_jobs.html', {'jobs': jobs})


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.user.is_staff:  # Admin ने job apply करू नये हे check केलं आहे:
        messages.error(request, "Admin users cannot apply for jobs.")
        return redirect('job_list')

    if Application.objects.filter(user=request.user, job=job).exists():  # Duplicate application चेक केलं आहे:
        messages.warning(request, "You have already applied for this job.")
        return redirect('job_list')

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.job = job
            application.save()

            # Form valid असला की application सेव्ह केलं आहे आणि email पाठवली आहे:
            send_mail(
                subject="Application Submitted Successfully",
                message=f'Hi {request.user.username},\n\n You have successfully applied for this job:{job.title}.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.user.email],
                fail_silently=False,
            )
            # Success message दाखवलं आहे आणि redirect केलं आहे:
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_list')
    else:
        form = ApplicationForm()

    return render(request, 'dashboard/apply_job.html', {'form': form, 'job': job})


@staff_member_required
def admin_dashboard(request):
    applications = Application.objects.all()
    return render(request, 'dashboard/admin_dashboard.html', {'applications': applications})




@staff_member_required
def update_status(request, application_id, status):
    application = get_object_or_404(Application, id=application_id)
    user = application.user  # this is a CustomUser instance

    # Now call the email function with required values
    send_status_email(user.email, user.username, status)

    #  Update the status
    application.status = status
    application.save()

    return redirect('admin_dashboard')  # Replace with your actual redirect


@staff_member_required
def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            return redirect('admin_dashboard')
    else:
        form = ApplicationForm()

    return render(request, 'dashboard/add_application.html', {'form': form})


@staff_member_required
def add_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        job_type = request.POST['job_type']
        salary_range = request.POST['salary_range']

        Job.objects.create(
            title=title,
            description=description,
            location=location,
            job_type=job_type,
            salary_range=salary_range
        )
        messages.success(request, "Job added successfully.")
        return redirect('job_list')  # किंवा तुमचं relevant URL

    return render(request, 'dashboard/add_job.html')



@login_required
def my_applications(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'dashboard/my_applications.html', {'applications': applications})


#edit add Job
@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully.')
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'dashboard/edit_job.html', {'form': form, 'job': job})




@login_required
def delete_job(request,job_id):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to delete jobs.")
        return redirect('job_list')
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    messages.success(request, 'Job deleted successfully.')
    return redirect('manage_jobs')



# Admin ने Status Update केल्यावर Email:

def send_status_email(user_email, user_name, status):
    subject = "Application Status"
    if status == "Approved":
        message = f"Dear {user_name},\n\nCongratulations! You have been shortlisted for the job."
    else:
        message = f"Dear {user_name},\n\nSorry! Your job application has been rejected."

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )


def Index(request):
    return render(request, 'myapp/index.html')


def about_view(request):
    total_candidates = CustomUser.objects.filter(role='candidate').count()
    total_jobs = Job.objects.count()
    total_filled_jobs = Application.objects.filter(status='Approved').count()
    total_companies = CustomUser.objects.filter(role='recruiter').count()

    context = {
        'total_candidates': total_candidates,
        'total_jobs': total_jobs,
        'total_filled_jobs': total_filled_jobs,
        'total_companies': total_companies,
    }
    return render(request, 'myapp/about.html', context)


def Contact(request):
    return render(request, 'myapp/contact.html')


# User Dashbord
@login_required
def user_dashboard(request):
    return render(request, 'dashboard/userdashbord.html', {'user': request.user})



# admin dashbord madhe old user delete



@login_required
def delete_application(request, app_id):
    try:
        if request.user.is_staff:
            application = get_object_or_404(Application, id=app_id)
            application.delete()
            messages.success(request, 'Application deleted successfully.')
            return redirect('admin_dashboard')
        else:
            application = get_object_or_404(Application, id=app_id, user=request.user)
            application.delete()
            messages.success(request, 'Application deleted successfully.')
            return redirect('my_applications')
    except Exception as e:
        messages.error(request, 'An error occurred while deleting the application.')
        return redirect('my_applications')



def messages_list(request):
    user_messages = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    return render(request, 'dashboard/messages/list.html', {'messages': user_messages})




def generate_otp():
    return str(random.randint(100000, 999999))

@login_required
def password_change_request(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            otp = generate_otp()
            request.session['otp'] = otp
            request.session['new_password'] = form.cleaned_data['new_password1']
            request.session['otp_created_at'] = time.time()

            send_mail(
                "OTP for Password Change",
                f"Your OTP is: {otp}",
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email],
                fail_silently=False,
            )
            messages.info(request, "OTP has been sent to your email.")
            return redirect('verify_password_otp')
    else:
        form = PasswordChangeForm(request.user)

    # ✅ This return was missing!
    return render(request, 'dashboard/change_password_form.html', {'form': form})




@login_required
def verify_password_otp(request):
    # Check if session data exists
    if 'otp' not in request.session or 'new_password' not in request.session:
        messages.error(request, "Invalid password change request. Please start again.")
        return redirect('change_password')

    # Check OTP expiration (5 minutes)
    if time.time() - request.session.get('otp_created_at', 0) > 300:
        request.session.pop('otp', None)
        request.session.pop('new_password', None)
        request.session.pop('otp_created_at', None)
        messages.error(request, "OTP has expired. Please request a new one.")
        return redirect('change_password')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '')
        if entered_otp == request.session['otp']:
            # OTP verified - change password
            user = request.user
            new_password = request.session['new_password']
            user.set_password(new_password)
            user.save()

            # Clear session
            request.session.pop('otp', None)
            request.session.pop('new_password', None)
            request.session.pop('otp_created_at', None)

            # Log out the user after password change
            logout(request)
            messages.success(request, "Password changed successfully. Please login with your new password.")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP. Please try again.")

    return render(request, 'dashboard/verify_password_otp.html')



@login_required
def resend_otp(request):
    if 'new_password' not in request.session:
        messages.error(request, "Session expired or invalid. Please try again.")
        return redirect('change_password')

    otp = generate_otp()
    request.session['otp'] = otp
    request.session['otp_created_at'] = time.time()

    send_mail(
        "New OTP for Password Change",
        f"Your new OTP is: {otp}",
        settings.DEFAULT_FROM_EMAIL,
        [request.user.email],
        fail_silently=False,
    )
    messages.info(request, "A new OTP has been sent to your email.")
    return redirect('verify_password_otp')



