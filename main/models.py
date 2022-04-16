from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    textile = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
