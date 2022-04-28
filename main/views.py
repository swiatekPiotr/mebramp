from django.shortcuts import render, redirect
from .models import Categories, Products
from .forms import ProductsForm

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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
    products = Products.objects.all()
    return render(request, 'main/product.html', {'single_product': single_product, 'products': products})


def add_product(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            add = form.save(commit=False)
            add.user = request.user
            add.save()
            return redirect('/add_product')
    else:
        form = ProductsForm()
    return render(request, 'main/add_product.html', {'form': form})


def update_product(request, product_id=None):
    if product_id is None:
        products = Products.objects.all()
        return render(request, 'main/update_product.html', {'products': products})
    else:
        update_product_obj = Products.objects.get(id=product_id)
        form = ProductsForm(request.POST or None, instance=update_product_obj)
        if form.is_valid():
            form.save()
        return render(request, 'main/update_product.html',
                      {'update_product_obj': update_product_obj,
                       'form': form})


def product_pdf(request, id):
    single_product = Products.objects.get(id=id)

    # create Bytestream buffer
    buf = io.BytesIO()
    # create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    # create blank list
    lines = [single_product.name, single_product.textile, single_product.description, ]

    # loop
    for line in lines:
        textobj.textLine(line)

    # finish up
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename=single_product.name+'.pdf')
