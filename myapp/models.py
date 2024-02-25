from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('host', 'Host'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True)  # Adding null=True to location field
    description = models.TextField(null=True)  # Adding null=True to description field
    # Add more fields as needed

class Job(models.Model):
    WORKING_TIMES_CHOICES = (
        ('fulltime', 'Full-time'),
        ('parttime', 'Part-time'),
    )

    company = models.ForeignKey(Company, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)  # Adding null=True to description field
    qualifications = models.TextField(null=True)  # Adding null=True to qualifications field
    requirements = models.TextField(null=True)  # Adding null=True to requirements field
    specifications = models.TextField(null=True)  # Adding null=True to specifications field
    working_times = models.CharField(max_length=10, choices=WORKING_TIMES_CHOICES)
    history = models.TextField(null=True)  
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='jobs', on_delete=models.CASCADE, default=1)

class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='applications', on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    cover_letter = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)
