from django.shortcuts import render
from django.http import HttpResponse

def book_ru(request):
    return HttpResponse("<h1>Русская книга: Война и мир</h1>")

def book_en(request):
    return HttpResponse("<h1>English Book: Harry Potter</h1>")

def book_usa(request):
    return HttpResponse("<h1>American Book: The Great Gatsby</h1>")

