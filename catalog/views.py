from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, HttpResponse

from catalog.models import Product


# Create your views here.

def home(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, '../templates/catalog/home.html', context=context)


def contacts(request):
    return render(request, '../templates/catalog/contacts.html')


def post_contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, number, message)
        return HttpResponse(f"Спасибо за обратную связь, {name}")
    return render(request, '../templates/catalog/contacts.html')


def product_info(request):
    return render(request,'../templates/catalog/product_info.html')


def product_index(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, '../templates/catalog/product_info.html', context=context)