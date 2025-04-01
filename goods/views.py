from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from goods.models import Categories, Products

def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else: 
        goods = Products.objects.filter(category__slug=category_slug)
        

    context = {
        'title': 'Каталог – Lilu',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
  
    product = Products.objects.get(slug=product_slug)
    
    context={
        'product': product
    }

    return render(request, 'goods/product.html', context=context)


