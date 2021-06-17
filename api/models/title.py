from textwrap import shorten
from django.db import models

from api.models.category import Category
from api.models.genre import Genre


class Title(models.Model):
    name = models.CharField(
        'title name',
        max_length=200,
        help_text='enter the title name'
    )
    year = models.IntegerField(
        'title year published',
        help_text='enter the title year published'
    )
    description = models.TextField(
        'title description',
        help_text='enter information about the title'
    )
    category = models.ForeignKey(
        Category,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='category',
        help_text='select a category'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles',
        verbose_name='genre',
        help_text='select a genre'
    )

    class Meta:
        app_label = 'api'
        verbose_name = 'titles'

    def __str__(self):
        shorten_comment_text = shorten(self.name, width=10, placeholder='...')
        return f'[{self.category}] {self.year}: {shorten_comment_text}'
