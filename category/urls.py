from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('category', CategoryViewAPI, basename='category_api')
# router.register('category-list', CategoryWithDetails, basename='category_api_list')
router.register('subcategory', SubCategoryViewAPI, basename='subcategory_api')
router.register('brand', BrandViewAPI, basename='brand_api')
router.register('type', TypeViewAPI, basename='type_api')
urlpatterns = [
     path('<int:category_id>/list', CategoryWithDetails.as_view(), name='category_with_details'),
    path('', include(router.urls)),
]