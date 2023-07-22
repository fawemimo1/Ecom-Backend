from django.contrib import admin
from .models import *

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class SizeInline(admin.StackedInline):
    model = Size
    extra = 1

class ColorInline(admin.StackedInline):
    model = Color
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, SizeInline, ColorInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(HomeBannerImage)


