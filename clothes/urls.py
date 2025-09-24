from django.urls import path
from . import views
from .views import ClothesListView

urlpatterns = [
    path('', ClothesListView.as_view(), name='clothes_list'),
]

