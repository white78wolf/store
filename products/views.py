from django.shortcuts import render

from products.models import ProductCategory, Product, Basket

def index(request):
    context = {
        'title': 'Store', 
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)

def basket_add(request, product_id):
    pass