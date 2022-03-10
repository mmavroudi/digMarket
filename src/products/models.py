from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(default='slug-field')  # unique=True
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True) #100.00
    sale_price = models.DecimalField(max_digits=100,
                                     decimal_places=2, default=6.99, null=True, blank=True)  # 100.00

    def __str__(self): #def_unicode_(self) in Python 2
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(default='slug_field')


    def __str__(self):
        return self.name
