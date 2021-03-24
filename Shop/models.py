from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe

from Account.models import Customer

class Brand(models.Model):
    brandName = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.brandName


class Category(models.Model):
    categoryName = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.categoryName


class Product(models.Model):
    demand = (
        ('Học tập - Văn phòng', 'Học tập - Văn phòng'),
        ('Đồ họa- Kĩ thuật', 'Đồ họa- Kĩ thuật'),
        ('Gaming', 'Gaming'),
        ('Cao cấp-Sang trọng', 'Cao cấp-Sang trọng'),
    )
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    price = models.PositiveBigIntegerField()
    quantity = models.IntegerField()
    quantitySelled = models.IntegerField(default=0)
    demand = models.CharField(max_length=200, null=True, choices=demand)
    dateAdded = models.DateTimeField(auto_now_add=True)
    Card = models.CharField(max_length=200, null=True)
    Screen = models.CharField(max_length=200, null=True)
    RAM = models.CharField(max_length=200, null=True)
    hard_disk = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    detail = RichTextUploadingField(null=True, blank=True)

    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True)

    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def get_total_product(self):
        sum = 0;
        cart_product = self.cart_product_set.all()
        for o in cart_product:
            sum = sum + o.quantity;
        return sum

    def get_total_price_product(self):
        sum = 0;
        cart_product = self.cart_product_set.all()
        for o in cart_product:
            sum += o.get_price_product();
        return sum;


class Cart_Product(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def get_price_product(self):
        return int(self.product.price * self.quantity)
