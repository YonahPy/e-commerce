from django.urls import path
from .views import ProductList, SubCategoryList, ProductDetail


urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('sub-category/', SubCategoryList.as_view(), name='sub-category-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-details')
]
