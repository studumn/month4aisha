from django.urls import path
from . import views
from .views import RegisterView, CustomLoginView, CustomLogoutView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
