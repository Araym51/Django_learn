from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title': 'Geekshop | Login'
    }

    return render(request, 'authapp/login.html', context)


def register(request):
    context = {
        'title': 'Geekshop | Register'
    }

    return render(request, 'authapp/register.html', context)