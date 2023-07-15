from django.db import models

# Create your models here.

class StoreInfo(models.Model):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    tiktok = models.CharField(max_length=200, null=True, blank=True)
    about_us = models.TextField(null=True, blank=True)
    shipping_policy = models.TextField(null=True, blank=True)
    refund_policy = models.TextField(null=True, blank=True)
    privacy_policy = models.TextField(null=True, blank=True)
    terms_of_service = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
