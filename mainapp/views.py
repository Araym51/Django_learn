from django.shortcuts import render
from django.views.generic import DetailView

from mainapp.models import Product, ProductCategory
import os
# Create your views here.

MODULE_DIR = os.path.dirname(__file__)

def index(request):
    context = {
        'title': 'Geekshop'
    }

    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Geekshop | каталог',
    }
    context['products'] = Product.objects.all()
    context['categories'] = ProductCategory.objects.all()
    # json_products = os.path.join(MODULE_DIR, 'fixtures/products.json')
    # context['product'] = json.load(open(json_products, encoding='utf-8'))

    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):

    model = Product
    template_name = 'mainapp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
