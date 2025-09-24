from django.contrib import admin
from .models import Movie, Comment

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_date', 'rating', 'tags')
    search_fields = ('title', 'genre', 'tags')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'created_at')



