from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .choices import state_choices
from django.http import HttpResponse
from django.forms.forms import Form


def add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    print(product)
    cart.add(product=product)
    print(cart.cart.items())
    return redirect("index")


def clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("detail")



def increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("detail")


def decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("detail")



def detail(request):
    if request.user.is_authenticated:
        return render(request,'cart/cart.html')
    return redirect('login')


def checkout(request):
    if request.method=='POST':
        print(request.POST)
    context={
        'state_choices':state_choices
    }
    return render(request,'cart/checkout.html',context)
