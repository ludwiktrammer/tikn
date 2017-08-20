from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin
from django import forms
from django.db import models

from .models import Book


@admin.register(Book)
class BookAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = (
        'title', 'cover', 'translator', 'original', 'edition', 'isbn',
        'circulation', 'price', 'store_id', 'embed', 'hidden',
    )
    list_display = ('title', 'translator', 'hidden')
    list_editable = ('hidden', )
    list_filter = ('hidden', 'translator', 'price')
    search_fields = ('title', 'translator', 'isbn')
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'style': 'min-width: 50%'}),
        },
    }
