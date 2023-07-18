from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewAPI, basename='product_api')
router.register('product_image', ProductImageViewAPI, basename='product_image_api')
router.register('product_detail', ProductDetailViewAPI, basename='product_detail_api')
router.register('image_fetch', ImageFetchAPIView, basename='image_fetch_api')
router.register('category_product_fetch', CategoryProductFetchAPIView, basename='category_product_fetch_api')
router.register('home_product', HomeProductAPIView, basename='home_product_api')
router.register('new_product', NewProductAPIView, basename='new_product_api')
router.register('top_product', TopProductAPIView, basename='top_product_api')
router.register('home_product_detail', HomeProductDetailAPIView, basename='home_product_detail_api')
router.register('new_product_detail', NewProductDetailAPIView, basename='new_product_detail_api')
router.register('top_product_detail', TopProductDetailAPIView, basename='top_product_detail_api')
router.register('new_product_image', NewProductImageAPIView, basename='new_product_image_api')
router.register('top_product_image', TopProductImageAPIView, basename='top_product_image_api')
router.register('home_product_image', HomeProductImageAPIView, basename='home_product_image_api')
router.register('home_banner_image', HomeBannerImageAPIView, basename='home_banner_image_api')
router.register('home_image_fetch', HomeImageFetchAPIView, basename='home_image_fetch_api')
router.register('top_image_fetch', TopImageFetchAPIView, basename='top_image_fetch_api')
router.register('new_image_fetch', NewImageFetchAPIView, basename='new_image_fetch_api')


urlpatterns = [
    path('', include(router.urls)),
]