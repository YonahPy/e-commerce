from django.urls import path
from .views import SubCategoryList, ProductDetail, ColorProductList, ProductListByCategory, SearchedProducts


urlpatterns = [
    path('sub-category/', SubCategoryList.as_view(), name='sub-category-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-details'),
    path('colors/', ColorProductList.as_view(), name='color-product'),
    path('products/category/<int:category>/', ProductListByCategory.as_view(), name='product-list-by-category'),
    path('products/search/<str:search>/', SearchedProducts.as_view(), name='searched-products'),
]
