from textwrap import shorten
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

    # TODO: create a separate method for this shortening
    def __str__(self):
        shorten_comment_text = shorten(self.text, width=10, placeholder='...')
        return f'[{self.pub_date}] {self.author}: {shorten_comment_text}'
# - id: skip
# - text: TextField
# - author: ForeignKey
# - pub_date: DateTimeField
#
# ------------
# * review ForeignKey
