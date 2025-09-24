from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.http import HttpResponse


def test_view(request):
    return HttpResponse("Cineboard работает!")

class MovieListView(ListView):
    model = Movie
    template_name = 'CineBoard/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = super().get_queryset()

        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genre=genre)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        queryset = queryset.order_by('-rating')
        return queryset


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'CineBoard/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'CineBoard/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.movie_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.kwargs['pk']})
