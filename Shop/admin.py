from django.contrib import admin
from .models import *


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('brand','category','quantity')
    list_display = ['name', 'brand', 'quantity']
    inlines = [ProductImageInline]
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer']


admin.site.register(Category)
admin.site.register(Cart,CartAdmin)
admin.site.register(Cart_Product)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Images)
