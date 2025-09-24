from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Movie(models.Model):
    GENRE_CHOICES = [
        ('horror', 'Ужасы'),
        ('drama', 'Мелодрама'),
        ('comedy', 'Комедия'),
        ('action', 'Боевик'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_date = models.DateField()
    rating = models.FloatField(default=0.0) 
    tags = models.CharField(max_length=200, blank=True)  

    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.movie.title}'
