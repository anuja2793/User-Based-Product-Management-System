from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register,name='register'),
    path('login/', views.user_login,name='login'),
    path('home/', views.home,name='home'),
    path('add/', views.add,name='add'),
    path('edit/', views.edit,name='edit'),
    path('logout/', views.user_logout,name='logout'),
    path('update/<int:id>/', views.update_product,name='update'),
    path('delete/<int:id>/', views.delete_product,name='delete'),
]
