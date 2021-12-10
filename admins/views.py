from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminUpdateDelete, \
    ProductAdminUpdateDelete
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

# Users
class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | ользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    title = 'Админка | Создать пользователя'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users_update')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Удалить пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)


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
