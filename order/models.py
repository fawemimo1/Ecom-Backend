from django.db import models
from product.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_data = models.JSONField(null=True, blank=True)
    products = models.JSONField(null=True, blank=True)
    order_id = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    cancel = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.order_id, self.email)
    
    class Meta:
        ordering = ['-created_at']  

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_data = models.JSONField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.order, self.created_at)
    
    class Meta:
        ordering = ['-created_at']  