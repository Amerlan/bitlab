from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField(default=100)
    description = models.TextField(null=True, default='Добавь описание')
    discount = models.FloatField(default=0.5)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}  {self.price}"


class Order(models.Model):
    customer = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(to=Product, null=True)
    is_active = models.BooleanField(default=True)


class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='customer')
    role = models.CharField(default="CLIENT", max_length=50)