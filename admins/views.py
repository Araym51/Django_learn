from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminUpdateDelete, \
    ProductAdminUpdateDelete
from authapp.models import User
from mainapp.models import ProductCategory, Product
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin


class IndexTemplateView(TemplateView, CustomDispatchMixin):
    template_name = 'admins/admin.html'


# Users
class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'Админка | Пользователи'


class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Создать пользователя'


class UserUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Редактирование пользователя'


class UserDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Удалить пользователя'


# Categories
@user_passes_test(lambda u: u.is_superuser)
def admin_category_read(request):

    context = {
        'categories':ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, pk):  # НЕ РАБОТАЕТ! Исправить!
    if request.method == 'POST':
        ProductCategory.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('admins:admin_category_read'))


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_products_read(request):
    context = {
        'title': 'Geekshop - Admin | Просмотр товаров '
    }
    context['products'] = Product.objects.all()
    return render(request, 'admins/admin-product-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateDelete(data=request.POST, instance=product_select, files=request.FILES)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, pk):
    if request.method == 'POST':
        Product.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('admins:product-read'))


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request): # прописать в urls
    if request.method == 'POST':
        form = ProductAdminUpdateDelete(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:product-read'))
    else:
        form = ProductAdminUpdateDelete()
    context = {
        'title': 'Geekshop - Admin | Product create',
        'form': form
    }
    return render(request, 'admins/admin-product-create.html', context)
