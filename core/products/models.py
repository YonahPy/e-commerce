from django.db import models

class CategoryPrimary(models.Model):
    name = models.CharField('nome', max_length=250)
    slug = models.SlugField('slug')
    description = models.CharField('descrição', max_length=400, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    name = models.CharField('nome', max_length=250)
    slug = models.SlugField('slug')
    category_primary = models.ForeignKey(CategoryPrimary, on_delete=models.CASCADE)
    description = models.CharField('descrição', max_length=400, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name

class ColorProduct(models.Model):
    color = models.CharField('Cor', max_length=100)
    url = models.URLField('Imagem da Cor')
    
    def __str__(self) -> str:
        return self.color
      
class Product(models.Model):
    web_id = models.IntegerField('Web ID')
    product_title = models.CharField('Titulo', max_length=400)
    image = models.URLField(verbose_name='Imagem')
    alternative_image = models.URLField('Imagem alternativa')
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    average_rating = models.FloatField('Média de avaliações')
    count_rating = models.IntegerField('Quantidade de avaliações')
    color = models.ManyToManyField(ColorProduct, verbose_name='Imagens das Cores Disponiveis', related_name='products')
    display_color = models.CharField('Cor atual', max_length=100)
    
    def __str__(self) -> str:
        return self.product_title
    
