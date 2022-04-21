from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path("search/", views.search, name='search'),
    path("<int:id>", views.category, name='index'),
]
