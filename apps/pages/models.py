from django.db import models
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse


class Page(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="nazwa",
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="identyfikator",
        help_text="wykorzystywane w adresie strony",
    )
    text = models.TextField(
        verbose_name="Treść",
        help_text=mark_safe("możesz używać znaczników formatowania <a href='http://commonmark.org/help/'>MarkDown</a>"),
    )
    menu = models.BooleanField(
        verbose_name="pokaż w menu",
        default=True,
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="kolejność",
    )

    class Meta:
        verbose_name = "strona"
        verbose_name_plural = "strony"
        ordering = ('order', "id")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={
            'slug': self.slug,
        })
