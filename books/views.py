from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import BookSearchForm
from django.core.paginator import Paginator

from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'page_obj'  
    paginate_by = 5  

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context



def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})



