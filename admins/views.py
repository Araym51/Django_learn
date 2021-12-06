from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminUpdateDelete, \
    ProductAdminUpdateDelete
from authapp.models import User
from mainapp.models import ProductCategory, Product

app_name = 'admins'


def index(request):
    return render(request, 'admins/admin.html')


def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form':form
    }
    return render(request,'admins/admin-users-create.html',context)


def admin_users_update(request,pk):

    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form':form,
        'user_select':user_select
    }
    return render(request, 'admins/admin-users-update-delete.html',context)


def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))


def admin_category_read(request):

    context = {
        'categories':ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)


def admin_category_update(request, pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryAdminUpdateDelete(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category_read'))
    else:
        form = CategoryAdminUpdateDelete(instance=category_select)
    context = {
        'title': 'Geekshop - Admin | Category update/delete',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'admins/admin-category-update-delete.html', context)


def admin_category_delete(request, pk):  # НЕ РАБОТАЕТ! Исправить!
    if request.method == 'POST':
        category = ProductCategory.objects.get(pk=pk)
        category.delete()
        category.save()

    return HttpResponseRedirect(reverse('admins:admin_category_read'))


def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminUpdateDelete(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category_read'))
    else:
        form = CategoryAdminUpdateDelete()
    context = {
        'title': 'Geekshop - Admin | Category Create',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)


def admin_products_read(request):
    context = {
        'title': 'Geekshop - Admin | Просмотр товаров '
    }
    context['products'] = Product.objects.all()
    return render(request, 'admins/admin-product-read.html', context)


def admin_products_update(request, pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateDelete(data=request.POST, instance=product_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:product-read'))
    else:
        form = ProductAdminUpdateDelete(instance=product_select)
    context = {
        'title': 'Geekshop - Admin | Product update/delete',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'admins/admin-product-update-delete.html', context)