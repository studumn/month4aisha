from django.urls import path
from . import views
from .views import TourListView, TourDetailView, tour_register

urlpatterns = [
    path('', TourListView.as_view(), name='tour_list'),
    path('<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
    path('register/<int:person_id>/', tour_register, name='tour_register'),
]

