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
from mainapp.mixin import BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin


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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Categories
class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'
    title = 'Админка - Список категорий'


class CategoryDeleteView(DeleteView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category_read')


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-update-delete.html'
    form_class = CategoryAdminUpdateDelete
    title = 'Админка | Обновления категории'
    success_url = reverse_lazy('admins:admin_category_read')


class CategoryCreateView(CreateView,BaseClassContextMixin, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_category_read')
    form_class = CategoryAdminUpdateDelete
    title = 'Админка | Создание категории'


#products
class ProductsListView(ListView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-product-read.html'
    title = 'Админка - Список продуктов'


class ProductUpdateView(UpdateView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    form_class = ProductAdminUpdateDelete
    title = 'Админка | Обновления родуктов'
    success_url = reverse_lazy('admins:product-read')


class ProductDeleteView(DeleteView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-product-update-delete.html'
    success_url = reverse_lazy('admins:product-read')


class ProductCreateView(CreateView, BaseClassContextMixin):
    model = Product
    template_name = 'admins/admin-product-create.html'
    success_url = reverse_lazy('admins:product-read')
    form_class = ProductAdminUpdateDelete
    title = 'Админка | Создание продуктов'
