from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField 

class CustomUserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'date_of_birth',
                  'address', 'position_applied', 'resume_link', 'education',
                  'experience_years', 'skills', 'linkedin_profile', 'portfolio_link', 'password1', 'password2']

