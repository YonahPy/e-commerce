# Generated by Django 4.2.6 on 2023-11-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20231105_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=300, null=True, unique=True, verbose_name='slug'),
        ),
    ]
