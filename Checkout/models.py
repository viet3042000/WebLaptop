from django.db import models

# Create your models here.
from Account.models import Customer
from Shop.models import Product


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('OnShipping', 'OnShipping'),
        ('Success', 'Success'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_finnish = models.DateTimeField(null=True, blank=True)
    date_ship = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='New')
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def get_total_price_product(self):
        sum = 0;
        order_product = self.order_product_set.all()
        for o in order_product:
            sum += o.get_price_product();
        return sum;


class Order_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)

    def get_price_product(self):
        return int(self.product.price * self.quantity)
