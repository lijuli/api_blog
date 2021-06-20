from django.db import models

from api.models.review import Review
from users.models import CustomUser


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='review',
        help_text='add a comment'
    )
    text = models.TextField(
        'comment text',
        help_text='enter your comment here'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='author'
    )
    pub_date = models.DateTimeField(
        'date published',
        auto_now_add=True
    )

    class Meta:
        app_label = 'api'
        verbose_name = 'comments'
        ordering = ('-pub_date',)
