# Generated by Django 3.0.5 on 2021-06-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210615_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(default='gpwlmagagv', max_length=10, verbose_name='Код подтверждения'),
        ),
    ]