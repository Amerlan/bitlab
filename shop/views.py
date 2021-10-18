from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product


class IndexView(APIView):
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'create_product.html'
    permission_classes = (AllowAny, )

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        context = {
            'products': serializer.data
        }
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print(data)
        product = Product.objects.create(**data)
        serializer = ProductSerializer(product)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)





def login_view(request):
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/product/')
        else:
            return redirect('/login/')
    else:
        return render(request, 'login.html')


def logout_view(request):
    print(request.POST)
    logout(request)
    return redirect('/login/')


def load_page_create_product(request):
    product = Product.objects.filter(price__gt=90)
    context = {
        "products": product
    }
    return render(request, 'create_product.html', context=context)


def create_product(request):
    data = request.POST
    name = data['name']
    price = data['price']
    description = data['description']
    try:
        product = Product.objects.get(name=name)
        product.price = price
        product.description = description
        product.save()
    except Exception:
        return redirect('/product/')
    # Product.objects.create(name=name, price=price, description=description)
    return redirect('/product/')


def show_users(request):
    return render('index.html')
