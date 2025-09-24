from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book  

def home(request):
    return render(request, "main_app/home.html")



