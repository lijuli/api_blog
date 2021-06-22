# Generated by Django 3.0.5 on 2021-06-20 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210620_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(help_text='add a title item', on_delete=django.db.models.deletion.CASCADE, related_name='review', to='api.Title', verbose_name='title'),
        ),
    ]
