from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path("search/", views.search, name='search'),
    path("<int:id>", views.category, name='index'),
    path("product/<int:id>", views.product, name='product'),
    path("add_product", views.add_product, name='add-product'),
    path("update_product", views.update_product, name='update-product'),
    path("update_product/<int:product_id>", views.update_product, name='update-product'),
    path("product/<int:id>/product_pdf", views.product_pdf, name='product-pdf'),
]
