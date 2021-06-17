# Generated by Django 3.0.5 on 2021-06-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, help_text='select a genre', null=True, related_name='titles', to='api.Genre', verbose_name='genre'),
        ),
    ]