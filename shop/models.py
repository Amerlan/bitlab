from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.TextField(null=True, default='Добавь описание')
    created = models.DateTimeField(auto_now=True)


class User(models.Model):
    name = models.CharField(max_length=40)
