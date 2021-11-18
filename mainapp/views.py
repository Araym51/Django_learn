from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Geekshop'
    }

    return render(request, 'index.html', context)


def products(request):
    context = {
        'title': 'Geekshop - каталог'
    }
    return render(request, 'products.html', context)
