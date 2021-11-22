from django.contrib.auth import logout, login
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .permissions import CustomerPermission, OrderCustomerPernission


class ProductViewSet(ModelViewSet):
    permission_classes = (CustomerPermission, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
    permission_classes = (OrderCustomerPernission,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def get(self, request):
        return super().list(request)

    def post(self, request):
        return super().create(request)


class OrderView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        order = get_object_or_404(Order, customer=request.user)
        serializer = OrderSerializer(order)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class AddProductApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        order, created = Order.objects.get_or_create(customer=request.user, is_active=True)
        order.product.add(product)
        return Response(status=status.HTTP_200_OK)


def homepage(request):
    return render(request, 'index.html')


def product_list(request):
    return render(request, 'product_list.html')


def product_detail(request, pk):
    return render(request, 'product_detail.html')


def order_detail(request):
    return render(request, 'order_detail.html')
