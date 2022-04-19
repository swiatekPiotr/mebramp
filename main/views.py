from django.shortcuts import render
from .models import Categories, Products


def home(request):
    return render(request, 'main/home.html', {})


def category(request, id):
    name_cat = Categories.objects.get(id=id)
    products = Products.objects.all()
    return render(request, 'main/category.html', {'name_cat': name_cat, 'products': products})
