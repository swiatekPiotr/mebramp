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
    product_image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    product_image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    product_image3 = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.TextField()
    textile = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
