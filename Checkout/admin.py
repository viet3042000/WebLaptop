from django.contrib import admin
from .models import Order_Product
from .models import Order


class OrderProductInline(admin.TabularInline):
    model = Order_Product
    readonly_fields = ['product', 'order', 'quantity']
    can_delete = False
    extra = 0


class Orderadmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'status', 'date_ship', 'date_finnish']
    search_fields = ('name',)
    list_filter = ['status']
    inlines = [OrderProductInline]


class OrderProductadmin(admin.ModelAdmin):
    list_display = ['product', 'order']


admin.site.register(Order, Orderadmin)
admin.site.register(Order_Product, OrderProductadmin)
