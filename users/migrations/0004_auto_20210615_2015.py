# Generated by Django 3.0.5 on 2021-06-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210615_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(default='reelacqnvy', max_length=10, verbose_name='Код подтверждения'),
        ),
    ]