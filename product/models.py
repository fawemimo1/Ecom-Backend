from django.db import models
from category.models import Category, Brand
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    cancel_price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    new = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)
    
class HomeProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    cancel_price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    new = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    visibility = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)

class NewProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    cancel_price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    new = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    visibility = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)

class TopProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    cancel_price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    visibility = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return str(self.product)
    
class HomeProductImage(models.Model):
    product = models.ForeignKey(HomeProduct, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return str(self.product)
    
class NewProductImage(models.Model):
    product = models.ForeignKey(NewProduct, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return str(self.product)
    
class TopProductImage(models.Model):
    product = models.ForeignKey(TopProduct, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return str(self.product)
    
class HomeBannerImage(models.Model):
    image = models.ImageField(upload_to='banner/')
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return str(self.image)