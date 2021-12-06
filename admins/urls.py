
from django.urls import path

from admins import views

app_name = 'admins'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.admin_users, name='admin_users'),
    path('users-create/', views.admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>', views.admin_users_update,name='admin_users_update'),
    path('users-delete/<int:pk>', views.admin_users_delete,name='admin_users_delete'),
    path('category-read/', views.admin_category_read, name='admin_category_read'),
    path('category-update/<int:pk>', views.admin_category_update, name='category-update' ),
    path('category-delete/<int:pk>', views.admin_category_delete, name='category-delete' ),
    path('category-create/', views.admin_category_create, name='category-create'),
    path('product-read/', views.admin_products_read, name='product-read'),
]

