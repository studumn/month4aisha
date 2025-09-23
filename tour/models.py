
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class TourRegistration(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    tour_name = models.CharField(max_length=200, default="Конный тур по Ала-Арче")
    registered_at = models.DateTimeField(auto_now_add=True)

class HorseTour(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
