from django.urls import path
from ordersapp import views

app_name = 'ordersapp'
urlpatterns = [
    path('', views.OrderList.as_view(), name='list'),
    path('create/', views.OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.OrderUpdate.as_view(), name='update'),
    path('read/<int:pk>/', views.OrderDetail.as_view(), name='read'),
    path('delete/<int:pk>/', views.OrderDelete.as_view(), name='delete'),
    path('forming_complete/<int:pk>/', views.order_forming_complete, name='forming_complete'),
]
