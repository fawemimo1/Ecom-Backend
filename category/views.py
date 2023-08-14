from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

class CategoryViewAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewAPI(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryDetailViewAPI(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryDetailSerializer

class BrandViewAPI(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailViewAPI(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer