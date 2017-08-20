import re

from django.db import models
from django.utils.functional import cached_property
from django.core.exceptions import ValidationError

from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize

SRC_REGEX = re.compile(r'\ssrc=["\']([^"\']+?)["\']')


def validate_has_src(value):
    if not SRC_REGEX.search(value):
        raise ValidationError("To nie jest poprawny kod embed flipstack.com!")


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="tytuł",
    )
    cover = models.ImageField(
        upload_to='covers/',
        verbose_name="okładka",
    )
    cover_list = ImageSpecField(
        source='cover',
        processors=[SmartResize(520, 730)],
        format='PNG',
    )
    translator = models.CharField(
        max_length=100,
        verbose_name="tłumaczka",
    )
    original = models.TextField(
        verbose_name="tytuł orginału",
        help_text="(i podstawa przekładu)",
    )
    edition = models.CharField(
        max_length=50,
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
    price = models.IntegerField(
        verbose_name="cena minimalna",
        blank=True,
        null=True,
    )
    store_id = models.IntegerField(
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

    class Meta:
        verbose_name = "książka"
        verbose_name_plural = "książki"
        ordering = ('-id', )

    def __str__(self):
        return self.title

    @cached_property
    def embed_url(self):
        if not self.embed:
            return None
        match = SRC_REGEX.search(self.embed)
        return match and match.group(1)
