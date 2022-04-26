from django import forms
from django.forms import ModelForm
from .models import Products


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ('category', 'name', 'product_image1', 'product_image2', 'product_image3',
                  'description', 'textile', 'price')
