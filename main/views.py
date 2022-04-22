from django.shortcuts import render
from .models import Categories, Products


def home(request):
    return render(request, 'main/home.html', {})


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Products.objects.filter(name__contains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'main/search.html', {})


def category(request, id):
    name_cat = Categories.objects.get(id=id)
    products = Products.objects.all()
    return render(request, 'main/category.html', {'name_cat': name_cat, 'products': products})


def product(request, id):
    single_product = Products.objects.get(id=id)
    return render(request, 'main/product.html', {'single_product': single_product})
