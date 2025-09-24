from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    position_applied = models.CharField(max_length=100, blank=True)
    resume_link = models.URLField(blank=True)
    education = models.CharField(max_length=100, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    skills = models.TextField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    portfolio_link = models.URLField(blank=True)
    
    def __str__(self):
        return self.username
