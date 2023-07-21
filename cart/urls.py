from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('wish_list', WishListViewSet, basename='cart_api')
router.register('wish_fetch', WishListFetchAPIView, basename='cart_fetch_api')

urlpatterns = [
    path('', include(router.urls)),
]
