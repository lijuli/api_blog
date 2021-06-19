from django.db import models

from api.models.title import Title
from users.models import CustomUser


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='review',
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
        related_name='review',
        verbose_name='author'
    )
    score = models.IntegerField(
        'review score',
        help_text='enter your review score'
    )
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True
    )

    class Meta:
        app_label = 'api'
        verbose_name = 'titles'
        ordering = ('-pub_date',)
