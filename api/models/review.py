from textwrap import shorten
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from api.models.title import Title
from users.models import CustomUser


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='title',
        help_text='add a title item'
    )
    text = models.TextField(
        'review text',
        help_text='enter your review here'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='author'
    )
    score = models.PositiveSmallIntegerField(
        'review score',
        validators=[
            MinValueValidator('Review score cannot be less than 1.', 1),
            MaxValueValidator('Review score cannot be greater than 10.', 10)
        ],
        help_text='enter your review score'
    )
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        app_label = 'api'
        verbose_name = 'reviews'
        ordering = ('-pub_date',)

    def __str__(self):
        shorten_review_text = shorten(self.name, width=10, placeholder='...')
        return f'[{self.category}] {self.year}: {shorten_review_text}'
