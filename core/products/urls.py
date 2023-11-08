from django.urls import path
from .views import ProductList, SubCategoryList
from . import views

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('sub-category/', SubCategoryList.as_view(), name='sub-category-list'),
    path('ola/', views.update_product_slugs, name='ola'),
    path('legal/', views.get_categories_data_api),
]
