from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from product.models import Product
# Create your models here.

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_data = models.JSONField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    clear = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.user, self.total)