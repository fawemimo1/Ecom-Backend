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
router.register('payment-detail', PaymentDetailAPIView, basename='payment-detail')
router.register('payment-success', PaymentSuccessFetchAPIView, basename='payment-success')
router.register('payment-pending', PaymentPendingFetchAPIView, basename='payment-pending')
router.register('payment-user', PaymentUserFetchAPIView, basename='payment-user')
router.register('payment-order', PaymentOrderFetchAPIView, basename='payment-order')
router.register('address', AddressViewSet, basename='address')
router.register('order-detail', OrderDetailViewSet, basename='order-detail')
router.register('order-fetch', OrderFetchAPIView, basename='order-fetch')
router.register('profile-fetch', ProfileFetchAPIView, basename='profile-fetch')
router.register('address-fetch', AddressFetchAPIView, basename='address-fetch')

urlpatterns = [
    path('', include(router.urls)),
    path('razorpay_order', PaymentView.as_view(), name='razorpay_order'),
    path('razorpay_callback', CallbackView.as_view(), name='razorpay_callback'),
    path('pincode_address/', PincodeAddressView.as_view(), name='pincode_address'),
    path('pincode_check/', PincodeCheckView.as_view(), name='pincode_check'),

]
