from django.shortcuts import render

import json
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
        'title': 'Geekshop - каталог',
    }
    json_products = os.path.join(MODULE_DIR, 'fixtures/products.json')
    context['product'] = json.load(open(json_products, encoding='utf-8'))
    return render(request, 'mainapp/products.html', context)
