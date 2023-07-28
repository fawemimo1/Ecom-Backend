from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryViewAPI, basename='category_api')
router.register('brand', BrandViewAPI, basename='brand_api')
router.register('brand-detail', BrandDetailViewAPI, basename='brand_api')
urlpatterns = [
    path('', include(router.urls)),
]