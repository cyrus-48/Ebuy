from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def products(request):
    template = loader.get_template('products/products.html')
    return HttpResponse(template.render({}, request))


def categories(request):
    template = loader.get_template('categories/categories.html')
    return HttpResponse(template.render({}, request))


def addProducts(request):
    return HttpResponse("<h2>You can add products here</h2>")


def deleteProduct(request):
    return HttpResponse("<h2> Hey there you can delete your product fro, this page</h2>")
