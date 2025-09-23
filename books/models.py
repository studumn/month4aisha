from django.db import models
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=20)
    pages = models.IntegerField(default=2025)
    language = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    year = models.IntegerField()


    def __str__(self):
        return self.title

