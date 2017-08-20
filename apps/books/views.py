from django.views.generic import ListView

from .models import Book


class BookList(ListView):
    model = Book
    queryset = Book.objects.filter(hidden=False)
    paginate_by = 3
