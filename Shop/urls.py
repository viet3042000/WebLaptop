from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('store/', views.Store, name='store'),
    path('update_item/', views.updateItem, name='update_item'),
    path('product/<int:id>/', views.product, name='product'),
    path('aboutUS/', views.aboutUs, name='aboutUs'),
    path('contact/', views.contact, name='contact'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('ordersandreturns/', views.ordersandreturns, name='ordersandreturns'),
    path('termandconditions/', views.termandconditions, name='termandconditions'),
    path('help/', views.help, name='help'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
