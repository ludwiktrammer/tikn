# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-05 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20170821_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='base',
            field=models.TextField(blank=True, help_text="możesz używać znaczników formatowania <a href='http://commonmark.org/help/'>MarkDown</a>", verbose_name='podstawa przekładu'),
        ),
        migrations.AddField(
            model_name='book',
            name='editor',
            field=models.CharField(blank=True, max_length=100, verbose_name='redakcja'),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, max_length=50, verbose_name='wydanie'),
        ),
        migrations.AlterField(
            model_name='book',
            name='original',
            field=models.TextField(blank=True, help_text="możesz używać znaczników formatowania <a href='http://commonmark.org/help/'>MarkDown</a>", verbose_name='tytuł orginału i podstawa przekładu'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(blank=True, max_length=100, verbose_name='przekład'),
        ),
    ]