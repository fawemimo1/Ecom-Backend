from django.db import models
from product.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Coupon(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True)
    title =  models.CharField(max_length=255)
    code =  models.CharField(max_length=255)
    description =  models.TextField(null=True,  blank =True)
    image = models.ImageField(upload_to='coupon-image/', null=True, blank=True)
    discount = models.FloatField(default=0)
    number_available = models.IntegerField(default=0)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, related_name='coupon_user', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    default = models.BooleanField(default=False)
    alternate_phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    address_type = models.CharField(max_length=255, default='home')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.user, self.address)

    class Meta:
        ordering = ['-created_at']

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_data = models.JSONField(null=True, blank=True)
    products = models.JSONField(null=True, blank=True)
    order_id = models.CharField(max_length=255, null=True, blank=True)
    user_address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    # phone = models.CharField(max_length=255, null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    shipped = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    out_for_delivery = models.BooleanField(default=False)
    returned = models.BooleanField(default=False)
    shipped_date = models.DateTimeField(null=True, blank=True)
    out_for_delivery_date = models.DateTimeField(null=True, blank=True)
    delivered_date = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    coupon = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.order_id)

    class Meta:
        ordering = ['-created_at']

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    provider_order_id = models.CharField(max_length=255)
    signature_id =  models.CharField(max_length=255)
    payment_id =  models.CharField(max_length=255)
    amount = models.FloatField()
    status = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.order, self.created_at)

    class Meta:
        ordering = ['-created_at']


