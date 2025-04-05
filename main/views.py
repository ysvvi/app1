from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная – Lilu'
        context['categories'] = Categories.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О нас – Lilu'
        return context
    
class DeliveryView(TemplateView):
    template_name = 'main/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title']='Оплата и доставка – Lilu',
        return context



# def index(request):
#     context = {
#         'title': 'Цветы с доставкой в Оренбурге – Lilu',
#     }

#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Салон цветов в Оренбурге – Lilu',
#     }

#     return render(request, 'main/about.html', context)


# def delivery(request):
#     context = {
#         'title': 'Салон цветов в Оренбурге – Lilu',
#     }

#     return render(request, 'main/delivery.html', context)
