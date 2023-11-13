from django.shortcuts import render
import requests
from rest_framework import generics
from .serializers import ProductSerializer, SubCategorySerializer
from .models import SubCategory, Product



class ProductList(generics.ListCreateAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


   