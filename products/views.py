from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse

from products.models import Products, Cart


def product(request):
    product = Products.objects.all().values()
    template = loader.get_template('products/products.html')
    context = {
        'product': product,
    }
    return HttpResponse(template.render(context, request))


def productdetails(request, pk):
    products = Products.objects.get(pk=pk)
    template = loader.get_template('products/productDetails.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))


def cart(request):
    productname = request.POST('name')
    image = request.POST('pimage')
    productprice = request.POST('price')
    cart = Cart(name=productname, pimage=image, price=productprice)
    cart.save()
    return HttpResponseRedirect(reverse('cart'))


def cartitems(request):
    cart = Cart.objects.all().values()
    template = loader.get_template('cart/cart.html')
    context = {
        'cart': cart,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    template = loader.get_template('categories/categories.html')
    return HttpResponse(template.render({}, request))


def addProducts(request):
    return HttpResponse("<h2>You can add products here</h2>")


def deleteProduct(request):
    return HttpResponse("<h2> Hey there you can delete your product fro, this page</h2>")


def cart(request):
    template = loader.get_template('cart/cart.html')
    return HttpResponse(template.render({}, request))
