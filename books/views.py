from django.shortcuts import render
from django.http import HttpResponse

def book_ru(request):
    return HttpResponse("<h1>Русская книга: Война и мир</h1>")

def book_en(request):
    return HttpResponse("<h1>English Book: Harry Potter</h1>")

def book_usa(request):
    return HttpResponse("<h1>American Book: The Great Gatsby</h1>")

from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
