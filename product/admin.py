from django.contrib import admin
from .models import *

class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

class HomeProductImageInline(admin.StackedInline):
    model = HomeProductImage
    extra = 1

class HomeProductAdmin(admin.ModelAdmin):
    inlines = [HomeProductImageInline]

class NewProductImageInline(admin.StackedInline):
    model = NewProductImage
    extra = 1

class NewProductAdmin(admin.ModelAdmin):
    inlines = [NewProductImageInline]

class TopProductImageInline(admin.StackedInline):
    model = TopProductImage
    extra = 1

class TopProductAdmin(admin.ModelAdmin):
    inlines = [TopProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(HomeProduct, HomeProductAdmin)
admin.site.register(NewProduct, NewProductAdmin)
admin.site.register(TopProduct, TopProductAdmin)
admin.site.register(HomeBannerImage)


