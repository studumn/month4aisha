
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views  
from books import views as books_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.register_view, name='register'),  
    path('accounts/', include('accounts.urls')),               
    path('basket/', include('basket.urls')),                 
    path('captcha/', include('captcha.urls')),               
    path('tour/', include('tour.urls')),              
    path('clothes/', include('clothes.urls')),
    path('books/', books_views.book_list, name='book_list'),       
]
