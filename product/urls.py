from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewAPI, basename='product_api')
router.register('product_image', ProductImageViewAPI, basename='product_image_api')
router.register('product_detail', ProductDetailViewAPI, basename='product_detail_api')

urlpatterns = [
    path('', include(router.urls)),
]