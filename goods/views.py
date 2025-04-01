from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from goods.models import Categories, Products

def catalog(request):

    categories=Categories.objects.all()

    goods = Products.objects.all()
    context = {
        'title': 'Каталог – Lilu',
        'categories': categories,
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):
  
    product = Products.objects.get(slug=product_slug)
    
    context={
        'product': product
    }

    return render(request, 'goods/product.html', context=context)


