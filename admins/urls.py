
from django.urls import path

from admins import views

app_name = 'admins'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    # users
    path('users/', views.UserListView.as_view(), name='admin_users'),
    path('users-create/', views.UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>', views.UserUpdateView.as_view(),name='admin_users_update'),
    path('users-delete/<int:pk>', views.UserDeleteView.as_view(),name='admin_users_delete'),
    # categories
    path('category-read/', views.CategoryListView.as_view(), name='admin_category_read'),
    path('category-update/<int:pk>', views.CategoryUpdateView.as_view(), name='category-update' ),
    path('category-delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category-delete' ),
    path('category-create/', views.CategoryCreateView.as_view(), name='category-create'),
    # products
    path('product-read/', views.admin_products_read, name='product-read'),
    path('product-update/<int:pk>', views.admin_products_update, name='product-update'),
    path('product-delete/<int:pk>', views.admin_product_delete, name='product-delete'),
    path('product-create/', views.admin_product_create, name='product-create'),
]

