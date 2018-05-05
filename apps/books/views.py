from django.views.generic import ListView, DetailView

from .models import Book


class BookList(ListView):
    model = Book
    queryset = Book.objects.filter(hidden=False)
    paginate_by = 24


class BookDetail(DetailView):
    model = Book
    queryset = Book.objects.filter(hidden=False)
