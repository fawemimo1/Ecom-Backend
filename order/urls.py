from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('payment', PaymentViewSet, basename='payment')
router.register('order-detail', OrderDetailViewSet, basename='order-detail')
router.register('order-fetch', OrderFetchAPIView, basename='order-fetch')
router.register('profile-fetch', ProfileFetchAPIView, basename='profile-fetch')

urlpatterns = [
    path('', include(router.urls)),
]
