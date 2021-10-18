from django.db import models
from django.db.models import Count


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(null=True, default='Добавь описание')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}  {self.price}"


class Order(models.Model):
    product = models.ManyToManyField(to=Product)


# class Product(models.Model):
#     name = models.CharField(max_length=40)
#     price = models.IntegerField()
#     description = models.TextField(null=True, default='Добавь описание')
#     created = models.DateTimeField(auto_now=True)
