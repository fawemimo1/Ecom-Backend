from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, null=True, blank=True, unique=False)
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['-date_created']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    alternate_number = models.CharField(max_length=255, null=True, blank=True)
    hint_name = models.CharField(max_length=255, null=True, blank=True)
    data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

    class Meta:
        ordering = ['-created_at']

@receiver(post_save, sender=User)
def create_shipping_address(sender, instance, created, **kwargs):
    if created:
        shipping_address_data = {
            'user': instance,
        }
        profile = Profile.objects.create(**shipping_address_data)

        # Associate the shipping address with the user
        instance.profile = profile
        instance.save()
