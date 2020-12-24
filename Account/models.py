from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name
