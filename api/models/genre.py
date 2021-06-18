from django.db import models


class Genre(models.Model):
    name = models.CharField(
        'genre name',
        max_length=200,
        help_text='enter the genre name'
    )
    slug = models.SlugField(
        'genre reference label',
        unique=True,
        help_text='enter the genre reference label'
    )

    class Meta:
        app_label = 'api'
        ordering = ('-pk',)

    def __str__(self):
        return self.name
