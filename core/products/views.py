from rest_framework import generics
from .serializers import ProductSerializer, SubCategorySerializer, ColorProductSerializer
from .models import SubCategory, Product, ColorProduct
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q 
    
class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all().order_by('name')
    serializer_class = SubCategorySerializer

class ColorProductList(generics.ListCreateAPIView):
    queryset = ColorProduct.objects.all()
    serializer_class = ColorProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListByCategory(generics.ListAPIView):
    
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        category_id = self.kwargs['category']
        return Product.objects.filter(category=category_id)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = PageNumberPagination()
        paginator.page_size = 24
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class SearchedProducts(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        search = self.kwargs['search']
        return Product.objects.filter(Q(product_title__icontains=search))