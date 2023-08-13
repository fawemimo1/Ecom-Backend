from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', ProductViewAPI, basename='product_api')
router.register('product_image', ProductImageViewAPI, basename='product_image_api')
router.register('image', ImageViewAPI, basename='image_api')
router.register('product_detail', ProductDetailViewAPI, basename='product_detail_api')
router.register('image_fetch', ImageFetchAPIView, basename='image_fetch_api')
router.register('colorimage_fetch', ColorImageFetchAPIView, basename='colorimage_fetch_api')
router.register('category_product_fetch', CategoryProductFetchAPIView, basename='category_product_fetch_api')
router.register('home_banner_image', HomeBannerImageAPIView, basename='home_banner_image_api')
router.register('size', SizeAPIView, basename='size_api')
router.register('color', ColorAPIView, basename='color_api')
router.register('search', SearchAPIView, basename='search_api')
router.register('home_product', HomeProductDetailViewAPI, basename='home_product_api')
router.register('picture', PictureAPIView, basename='picture_api')
urlpatterns = [
    path('', include(router.urls)),
]