
from django.db import models
# from books.models import Book 

STATUS_CHOICES = [
    ('Выполнено', 'Выполнено'),
    ('Не выполнено', 'Не выполнено'),
]

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    card_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Не выполнено')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
