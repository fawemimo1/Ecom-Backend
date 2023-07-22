from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

# admin.site.site_header = 'NCPLISO'
# admin.site.index_title = 'NCPLISO'
# admin.site.site_title = 'NCPLISO'


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'country', 'zip_code', 'admin')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'country', 'zip_code', 'admin')}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(ShippingAddress)
