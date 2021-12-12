
from django.urls import path
from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.LoginListView.as_view(),name='login'),
    path('register/', views.RegisterListView.as_view(),name='register'),
    path('profile/', views.ProfileFormView.as_view(), name='profile'),
    path('logout/', views.Logout.as_view(), name='logout'),
]

