from django.db import models


class Category(models.Model):
    name = models.CharField(
        'category name',
        max_length=200,
        help_text='enter the category name'
    )
    slug = models.SlugField(
        'category reference label',
        unique=True,
        help_text='enter the category reference label'
    )

    class Meta:
        app_label = 'api'
        ordering = ('-pk',)

    def __str__(self):
        return self.name
