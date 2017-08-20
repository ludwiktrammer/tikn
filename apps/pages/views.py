from django.views.generic import DetailView

from .models import Page


class PageDetail(DetailView):
    model = Page
