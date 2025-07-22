from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .models import CustomUser, Job, Application
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Job)
admin.site.register(Application)


