from rest_framework import *
from django.contrib.auth.models import *
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # price = serializers.IntegerField()
    # price_with_discount = serializers.SerializerMethodField()

    # def get_price_with_discount(self, obj):
    #     return obj.price * obj.discount

    class Meta:
        model = Product
        fields = ('name', 'price')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    customer = CustomerSerializer()

    class Meta:
        fields = ('customer', 'id')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'