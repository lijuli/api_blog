# Generated by Django 3.0.5 on 2021-06-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_auto_20210617_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(blank=True, default='aefpfzrpec', max_length=10, null=True, verbose_name='Код подтверждения'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]