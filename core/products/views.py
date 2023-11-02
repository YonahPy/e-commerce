from django.shortcuts import render
import requests
from django.http import HttpResponse

def get_categories_data_api(request):
    if request.method == 'GET':
        url = "https://kohls.p.rapidapi.com/categories/list"
        
        headers = {
            "X-RapidAPI-Key":"3a2ceeee43msh2e5d34d8684068fp18367fjsn0121647ebf82",
            
            "X-RapidAPI-Host": "kohls.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        
        data = response.json()
        categories = data['payload']['categories']
        main_categories = []
        
        for categorie in categories:
            if categorie['name'] in ['Home','Women', 'Men', 'Kids, Baby & Toys']:
                main_categories.append(categorie)
        
        
        return main_categories
        



