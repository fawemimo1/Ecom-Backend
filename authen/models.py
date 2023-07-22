from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, null=True, blank=True, unique=False)
    admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.username)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

		