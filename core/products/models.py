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