# from textwrap import shorten
# from django.db import models
#
# from api.models.title import Title
# from users.models import CustomUser
#
#
# class Review(models.Model):
#     title = models.ForeignKey(
#         Title,
#         blank=True,
#         null=True,
#         on_delete=models.CASCADE,
#         related_name='review',
#         verbose_name='title',
#         help_text='add a title item'
#     )
#     text = models.TextField(
#         'review text',
#         help_text='enter your review here'
#     )
#     author = models.ForeignKey(
#         CustomUser,
#         on_delete=models.CASCADE,
#         related_name='review',
#         verbose_name='author'
#     )
#     score = models.FloatField()
#     pub_date = models.DateTimeField(
#         'date published',
#         auto_now_add=True
#     )
#
#     class Meta:
#         app_label = 'api'
#         verbose_name = 'titles'
#         ordering = ('-pub_date',)
#
#     def __str__(self):
#         shorten_comment_text = shorten(self.text, width=10, placeholder='...')
#         return f'[{self.pub_date}] {self.author}: {shorten_comment_text}'

# - id skip
# - text: TextField
# - author: ForeignKey
# - score: FloatField
# - pub_date: DateTimeField
#
# ------------
# * review ForeignKey
