# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20170821_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(help_text='wykorzystywane w adresie strony', max_length=100, unique=True, verbose_name='identyfikator'),
        ),
    ]