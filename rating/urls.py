from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('rating', RatingViewAPI, basename='rating_api')

urlpatterns = [
    path('', include(router.urls)),
]
