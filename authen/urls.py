from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("user", UserViewAPI.as_view({
        'get': 'list',
    }), name="user_list"),
    path("user/<int:pk>", UserViewAPI.as_view({'get': 'retrieve', 'put': 'update',
                                               'patch': 'partial_update',
                                               'delete': 'destroy'}), name='user_api'),
    path('login', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', LogoutAndBlacklistRefreshToken.as_view(), name='blacklist_token'),
    path('change_password/<int:id>', ChangePasswordView.as_view(),
         name='auth_change_password'),
    path('register',
         RegisterView.as_view({'post': 'create'}), name='auth_register'),
    path('shipping_address', ShippingAddressViewAPI.as_view({
        'get': 'list',
        'post': 'create'
    }), name='shipping_address_list'),
    path('shipping_address/<int:pk>', ShippingAddressViewAPI.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='shipping_address_api'),

    path('send-sms/', SendSMS.as_view(), name='send-sms'),
]
