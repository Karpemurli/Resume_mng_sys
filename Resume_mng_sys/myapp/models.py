from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from datetime import timedelta,timezone



# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='candidate')
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    @property
    def is_candidate(self):
        return self.role == 'candidate'

    @property
    def is_recruiter(self):
        return self.role == 'recruiter'

    @property
    def is_admin(self):
        return self.role == 'admin'



class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    ]
    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        default='Full-time'
    )

    salary_range = models.CharField(
        max_length=100,
        default='Not specified'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Job"


class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey('myapp.CustomUser', on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"

    class Meta:
        verbose_name_plural = "Application"


class Customer(models.Model):  # ✅ Use basic Model here
    user = models.OneToOneField('myapp.CustomUser', on_delete=models.CASCADE)