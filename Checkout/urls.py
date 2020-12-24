from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('orderdetail/<int:id>/', views.orderdetail, name='orderdetail'),
    path('update_order/', views.update_order, name='update_order'),

]
