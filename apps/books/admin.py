from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin
from django import forms
from django.db import models

from .models import Book


@admin.register(Book)
class BookAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'author', 'title', 'description', 'cover', 'translator', 'editor', 'original',
                'base', 'edition', 'isbn', 'circulation', 'price', 'store_id', 'embed',
            )
        }),
        ('Zaawansowane', {
            'classes': ('collapse',),
            'fields': ('slug', 'hidden'),
        }),
    )
    list_display = ('title', 'author', 'hidden')
    list_editable = ('hidden', )
    list_filter = ('hidden', 'translator', 'author', 'price')
    search_fields = ('title', 'author', 'translator', 'isbn')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'style': 'min-width: 50%'}),
        },
    }
