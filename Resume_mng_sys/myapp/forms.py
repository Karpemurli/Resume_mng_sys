from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model,SetPasswordForm
from .models import CustomUser, Application, Job


class CandidateRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=15, required=False)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)
    country = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'email', 'phone',
            'gender', 'address', 'country', 'state', 'city',
            'password1', 'password2'
        ]


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume']




class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'location', 'job_type', 'salary_range']


# update Register

CustomUser = get_user_model()


class RegisterUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'gender', 'address', 'city', 'state', 'country']
        widgets = {
            'gender': forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
        }

class ChangePasswordWithOTPForm(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any additional customization here
        self.fields['new_password1'].help_text = "Enter a strong password"
        self.fields['new_password2'].help_text = "Enter the same password as above"