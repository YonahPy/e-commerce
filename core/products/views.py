from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import SubCategory, Product, ColorProduct, CategoryPrimary

def get_categories_data_api(request):
    if request.method == 'GET':
        url = "https://kohls.p.rapidapi.com/products/list"

        querystring = {"limit":"24","offset":"1","keyword":"women tops"}

        headers = {
            "X-RapidAPI-Key": "3a2ceeee43msh2e5d34d8684068fp18367fjsn0121647ebf82",
            "X-RapidAPI-Host": "kohls.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()
        
        list_products = data['payload']['products']
         
        
        for item in list_products:
            
            sub_category = SubCategory.objects.get(id=6)
            prices = item['prices'] 
            regular_price = prices[0]['regularPrice'] 
            min_price = regular_price['minPrice'] 
            
            products = Product.objects.create(
                web_id=item['webID'],
                product_title=item['productTitle'],
                category=sub_category,
                image=item['image']['url'],
                alternative_image=item['altImageUrl'],
                price=min_price,
                average_rating=item['rating']['avgRating'],
                count_rating=item['rating']['count'],
                display_color=item['displayColor']
            )
            
            
            colors = item['swatchImages']
            for color_info in colors:
                color_name = color_info['color']
                color_url = color_info['URL']
                color_product, created = ColorProduct.objects.get_or_create(color=color_name, url=color_url)
                products.color.add(color_product)
                
            products.save()
            color_product.save()
            
        return list_products
        



