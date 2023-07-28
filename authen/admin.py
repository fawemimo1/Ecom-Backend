from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.



class CustomUserAdmin(UserAdmin):
    list_display = ['username',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('admin','active',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ( 'admin','active',)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
