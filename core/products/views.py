from rest_framework import generics
from .serializers import ProductSerializer, SubCategorySerializer, ColorProductSerializer
from .models import SubCategory, Product, ColorProduct

    
    
class SubCategoryList(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
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
   