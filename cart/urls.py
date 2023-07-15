from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cart', CartViewSet, basename='cart')
router.register('cart-fetch', CartFetchAPIView, basename='cart-fetch')

urlpatterns = [
    path('', include(router.urls)),
]