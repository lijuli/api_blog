import datetime
from textwrap import shorten
from django.core.exceptions import ValidationError
from django.db import models

from api.models.category import Category
from api.models.genre import Genre


class Title(models.Model):
    def validate_year(year):
        if year > datetime.datetime.now().year:
            raise ValidationError(
                'Select past or current year.The future is yet to come.'
            )

    name = models.CharField(
        'title name',
        max_length=200,
        help_text='enter the title name'
    )
    year = models.IntegerField(
        'title year published',
        blank=True,
        null=True,
        validators=[validate_year],
        help_text='enter the title year published'
    )
    description = models.TextField(
        'title description',
        blank=True,
        null=True,
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
        ordering = ('-pk',)

    def __str__(self):
        shorten_title_text = shorten(self.name, width=10, placeholder='...')
        return f'[{self.category}] {self.year}: {shorten_title_text}'
