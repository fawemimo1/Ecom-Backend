from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _

class User(AbstractUser):
    username = models.CharField(max_length=255, null=True, blank=True, unique=False)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Remove 'username' from the list

    def __str__(self):
        return str(self.email)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

		