from rest_framework import serializers
from .models import Product, SubCategory, ColorProduct

       
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ColorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorProduct
        fields = '__all__'
 
        
class ProductSerializer(serializers.ModelSerializer):
    color = ColorProductSerializer(many=True)
    name_category = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_name_category(self, obj):
        return obj.name_category()