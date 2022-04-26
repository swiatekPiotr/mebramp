from django import forms
from django.forms import ModelForm
from .models import Products


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'name', 'product_image1', 'product_image2', 'product_image3',
                  'description', 'textile', 'price']
        labels = {
            'product_image1': 'img 1', 'product_image2': 'img 2', 'product_image3': 'img 3',
            'description': '', 'textile': '', 'price': '',
        }
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'short description about product'}),
            'textile': forms.TextInput(attrs={'placeholder': 'textile'}),
            'price': forms.NumberInput(attrs={'placeholder': 'price'}),
        }
