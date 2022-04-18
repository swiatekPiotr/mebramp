from django.contrib import admin
from .models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "category", "name"]
    list_filter = ["category"]
