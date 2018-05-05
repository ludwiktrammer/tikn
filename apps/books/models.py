import re
import os
import unicodedata

from django.db import models
from django.utils.functional import cached_property
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.deconstruct import deconstructible
from django.utils.safestring import mark_safe

from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize

SRC_REGEX = re.compile(r'\ssrc=["\']([^"\']+?)["\']')


def validate_has_src(value):
    if not SRC_REGEX.search(value):
        raise ValidationError("To nie jest poprawny kod embed flipstack.com!")


def remove_unicode(path):
    def wrapper(instance, filename):
        filename = unicodedata.normalize('NFKD', filename) \
            .encode('ascii', 'ignore').decode('ascii')
        return os.path.join(path, filename)
    return wrapper


@deconstructible
class PathAndRemoveUnicode(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        filename = unicodedata.normalize('NFKD', filename) \
            .encode('ascii', 'ignore').decode('ascii')
        return os.path.join(self.path, filename)


class Book(models.Model):
    author = models.CharField(
        max_length=100,
        verbose_name="autor",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="tytuł",
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="identyfikator",
        help_text="wykorzystywane w adresie strony",
    )
    description = models.TextField(
        verbose_name="Opis",
        help_text=mark_safe("możesz używać znaczników formatowania <a href='http://commonmark.org/help/'>MarkDown</a>"),
    )
    cover = models.ImageField(
        upload_to=PathAndRemoveUnicode('covers/'),
        verbose_name="okładka",
    )
    cover_list = ImageSpecField(
        source='cover',
        processors=[SmartResize(520, 730)],
        format='PNG',
    )
    translator = models.CharField(
        max_length=100,
        verbose_name="przekład",
        blank=True,
    )
    editor = models.CharField(
        max_length=100,
        verbose_name="redakcja",
        blank=True,
    )
    original = models.TextField(
        verbose_name="tytuł orginału i podstawa przekładu",
        blank=True,
        help_text=mark_safe("możesz używać znaczników formatowania <a href='http://commonmark.org/help/'>MarkDown</a>"),
    )
    base = models.TextField(
        verbose_name="podstawa wydania",
        blank=True,
        help_text=mark_safe("możesz używać znaczników formatowania <a href='http://commonmark.org/help/'>MarkDown</a>"),
    )
    edition = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="wydanie",
    )
    isbn = models.CharField(
        max_length=18,
        verbose_name="ISBN",
        blank=True,
    )
    circulation = models.CharField(
        max_length=50,
        verbose_name="nakład",
        blank=True,
    )
    price = models.PositiveIntegerField(
        verbose_name="cena minimalna",
        blank=True,
        null=True,
    )
    store_id = models.PositiveIntegerField(
        verbose_name="ID w sklepie",
        help_text="product_id z adresu produktu na bractwotrojka.pl",
        blank=True,
        null=True,
    )
    embed = models.TextField(
        verbose_name="Kod embed książki",
        help_text="wygenerowany na flipstack.com",
        validators=[validate_has_src],
        blank=True,
        null=True,
    )
    hidden = models.BooleanField(
        verbose_name="ukryj na stronie",
        default=False,
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="kolejność",
    )

    class Meta:
        verbose_name = "książka"
        verbose_name_plural = "książki"
        ordering = ('-order', '-id')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={
            'slug': self.slug,
        })

    @cached_property
    def embed_url(self):
        if not self.embed:
            return None
        match = SRC_REGEX.search(self.embed)
        return match and match.group(1)
