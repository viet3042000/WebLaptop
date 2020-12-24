from django.urls import path
from . import views

urlpatterns = [
    path('update_user/', views.updateUser, name='updateUser'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('adminbrands/', views.adminbrands, name='adminbrands'),
    path('admincategory/', views.admincategory, name='admincategory'),
    path('adminproducts/', views.adminproducts, name='adminproducts'),
    path('adminorders/', views.adminorders, name='adminorders'),
    path('admincustomers/', views.admincustomers, name='admincustomers'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
]
