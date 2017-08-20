from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin
from django import forms
from django.db import models

from .models import Page


@admin.register(Page)
class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'text')
        }),
        ('Zaawansowane', {
            'classes': ('collapse',),
            'fields': ('slug', 'menu'),
        }),
    )
    list_display = ('name', 'menu')
    list_editable = ('menu', )
    list_filter = ('menu', )
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'style': 'min-width: 50%'}),
        },
    }
