from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views  
from books import views as books_views

urlpatterns = [
    path('admin/', admin.site.urls),
    

    path('', accounts_views.RegisterView.as_view(), name='home'),  
    
   
    path('register/', accounts_views.RegisterView.as_view(), name='register'),  
    path('login/', accounts_views.CustomLoginView.as_view(), name='login'),      
    path('logout/', accounts_views.CustomLogoutView.as_view(), name='logout'),   
    path("accounts/", include("django.contrib.auth.urls")),   
    path('accounts/', include('accounts.urls')),               
    path('basket/', include('basket.urls')),                 
    path('captcha/', include('captcha.urls')),               
    path('tour/', include('tour.urls')),              
    path('clothes/', include('clothes.urls')),
    path('cineboard/', include('cineboard.urls')),  
    
]
