from django.contrib import admin
from .models import Order, Payment, Coupon, Address
# Register your models here.

admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Address)