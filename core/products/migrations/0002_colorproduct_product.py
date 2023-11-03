# Generated by Django 4.2.6 on 2023-11-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100, verbose_name='Cor')),
                ('url', models.URLField(verbose_name='Imagem da Cor')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_id', models.IntegerField(verbose_name='Web ID')),
                ('product_title', models.CharField(max_length=400, verbose_name='Titulo')),
                ('image', models.URLField(verbose_name='Imagem')),
                ('alternative_image', models.URLField(verbose_name='Imagem alternativa')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('average_rating', models.FloatField(verbose_name='Média de avaliações')),
                ('count_rating', models.IntegerField(verbose_name='Quantidade de avaliações')),
                ('display_color', models.CharField(max_length=100, verbose_name='Cor atual')),
                ('color', models.ManyToManyField(related_name='products', to='products.colorproduct', verbose_name='Imagens das Cores Disponiveis')),
            ],
        ),
    ]
