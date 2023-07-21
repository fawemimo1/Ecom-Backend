from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import date
from django.utils.translation import gettext as _

class User(AbstractUser):
	email = models.EmailField(_('email address'), unique = True)
	phone_number = models.CharField(max_length=15, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)
	zip_code = models.CharField(max_length=10, null=True, blank=True)
	admin = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	def __str__(self):
		return str(self.email)
	