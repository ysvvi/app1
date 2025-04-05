from django.db.models import F, DecimalField, ExpressionWrapper
from django.http import Http404
from django.views.generic import DetailView, ListView

from goods.models import Products
from goods.utils import q_search


class CatalogView(ListView):
    model = Products
    # queryset = Products.objects.all().order_by("-id")
    template_name = "goods/catalog.html"
    context_object_name = "goods"
    paginate_by = 3
    allow_empty = False
    # чтоб удобно передать в методы

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        if category_slug == "all":
            goods = super().get_queryset()
        elif query:
            goods = q_search(query)
        else:
            goods = super().get_queryset().filter(category__slug=category_slug)
            if not goods.exists():
                raise Http404()

        if on_sale:
            goods = goods.filter(discount__gt=0)

        if order_by and order_by != "default":
            if order_by == "price":
                # Создаем аннотацию для сортировки по цене с учетом скидки
                goods = goods.annotate(
                    discounted_price=ExpressionWrapper(F('price') - F('price') * F('discount') / 100, output_field=DecimalField())
                ).order_by('discounted_price')
            elif order_by == "-price":
                goods = goods.annotate(
                    discounted_price=ExpressionWrapper(F('price') - F('price') * F('discount') / 100, output_field=DecimalField())
                ).order_by('-discounted_price')
            else:
                goods = goods.order_by(order_by)

        return goods
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Каталог – Lilu"
        context["slug_url"] = self.kwargs.get("category_slug")
        return context


class ProductView(DetailView):

    # model = Products
    # slug_field = "slug"
    template_name = "goods/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context