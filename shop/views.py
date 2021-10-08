from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Product


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
    product = Product.objects.first()
    context = {
        "product": product
    }
    return render(request, 'create_product.html', context=context)


def create_product(request):
    data = request.POST
    name = data['name']
    price = data['price']
    description = data['description']
    Product.objects.create(name=name, price=price, description=description)
    return redirect('/product/')


def show_users(request):
    return render('index.html')
