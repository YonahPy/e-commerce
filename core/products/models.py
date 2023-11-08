from django.db import models
from django.utils.text import slugify

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
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, default=1)
    image = models.URLField(verbose_name='Imagem')
    alternative_image = models.URLField('Imagem alternativa', null=True, blank=True)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    average_rating = models.FloatField('Média de avaliações', null=True, blank=True)
    count_rating = models.IntegerField('Quantidade de avaliações', null=True, blank=True)
    color = models.ManyToManyField(ColorProduct, verbose_name='Imagens das Cores Disponiveis', related_name='products')
    display_color = models.CharField('Cor atual', max_length=100)
    slug = models.SlugField('slug', unique=True, null=True, blank=True, max_length=300)
    
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.product_title}/'
    
    def create_slug(self, *args, **kwargs):
        self.slug = slugify(self.product_title)
        super(Product, self).save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return self.product_title
    
