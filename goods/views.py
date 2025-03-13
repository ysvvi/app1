from django.shortcuts import render
from django.http import HttpResponse
from django.template import context


def catalog(request):
    context = {
        'title': 'Каталог – Lilu',
        'goods': [
        {
            'image': 'deps/images/5.jpg',
            'name': 'Чайный столик и три стула',
            'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
            'price': 150
        },

         {
             'image': 'deps/images/5.jpg',
            'name': 'Чайный столик и два стула',
            'description': 'Набор из стола и двух стульев в минималистическом стиле.',
            'price': 93
        },

         {
             'image': 'deps/images/5.jpg',
         'name': 'Двухспальная кровать',
         'description': 'Кровать двухспальная с надголовником и вообще очень ортопедичная.',
         'price': 670},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Кухонный стол с раковиной',
         'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
         'price': 365},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Кухонный стол с встройкой',
         'description': 'Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.',
         'price': 430},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Угловой диван для гостинной',
         'description': 'Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!',
         'price': 610},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Прикроватный столик',
         'description': 'Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).',
         'price': 55},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Диван обыкновенный',
         'description': 'Диван, он же софа обыкновенная, ничего примечательного для описания.',
         'price': 190},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Стул офисный',
         'description': 'Описание товара, про то какой он классный, но это стул, что тут сказать...',
         'price': 30},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Растение',
         'description': 'Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.',
         'price': 10},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Цветок стилизированный',
         'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
         'price': 15},

         {
             'image': 'deps/images/5.jpg',
         'name': 'Прикроватный столик',
         'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
         'price': 25},
        ]
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')

# Create your views here.
