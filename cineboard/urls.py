from django.urls import path
from . import views
from .views import MovieListView, MovieCreateView, MovieDetailView, MovieUpdateView, MovieDeleteView, AddCommentView


urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie_list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('add/', views.MovieCreateView.as_view(), name='movie_add'),
    path('<int:pk>/edit/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
]

