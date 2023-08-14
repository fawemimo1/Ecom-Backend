from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('coupon', CouponListViewSet, basename='coupon-list')
router.register('available-coupon', AvailableCouponListViewSet, basename='available-coupon-list')
router.register('coupon-admin', CouponViewSet, basename='coupon')
router.register('fetch-coupon', FetchCouponViewSet, basename='fetch-coupon')
router.register('payment', PaymentViewSet, basename='payment')
router.register('address', AddressViewSet, basename='address')
router.register('order-detail', OrderDetailViewSet, basename='order-detail')
router.register('order-fetch', OrderFetchAPIView, basename='order-fetch')
router.register('profile-fetch', ProfileFetchAPIView, basename='profile-fetch')
router.register('address-fetch', AddressFetchAPIView, basename='address-fetch')

urlpatterns = [
    path('', include(router.urls)),
]
