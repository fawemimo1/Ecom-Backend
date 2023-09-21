from django.db import models
from category.models import Category, Brand,  SubCategory, CategoryType
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    cancel_price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    discount = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    top_product = models.BooleanField(default=False)
    new_product = models.BooleanField(default=False)
    home_product = models.BooleanField(default=False)
    show_size = models.BooleanField(default=False)
    show_color = models.BooleanField(default=False)
    show_gender = models.BooleanField(default=False)
    color_image = models.JSONField(null=True)
    size = models.JSONField(null=True)
    gender =  models.JSONField(null=True)
    color =  models.JSONField(null=True)
    available_quantity = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)
    category_type = models.ForeignKey(CategoryType, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.price)

    class Meta:
        ordering = ['-created_at']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/', null=True, blank=True)

    def __str__(self):
        return str(self.product)

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='imagescolor', on_delete=models.CASCADE, null=True, blank=True)
    color = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    data = models.JSONField(null=True, blank=True)

class Picture(models.Model):
    image = models.ImageField(upload_to='image/', null=True, blank=True)

class HomeBannerImage(models.Model):
    image = models.ImageField(upload_to='banner/')
    visibility = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.image)


class Size(models.Model):
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
    size = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.size)

class Color(models.Model):
    product = models.ForeignKey(Product, related_name='colors', on_delete=models.CASCADE)
    color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.color)