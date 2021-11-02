from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()

    class Meta:
        fields = (
            'email', 'message',
        )
