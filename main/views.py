from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Цветы с доставкой в Оренбурге – Lilu',
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Про нас – Lilu',
    }

    return render(request, 'main/about.html', context)

def delivery(request):
    context = {
        'title': 'Оплата и доставка – Lilu',
    }

    return render(request, 'main/delivery.html', context)
