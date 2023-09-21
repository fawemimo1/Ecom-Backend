from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

class CategoryViewAPI(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

class SubCategoryViewAPI(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SubCategoryDetailSerializer
        return SubCategorySerializer

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        category_type = self.request.query_params.get('category_type')
        if category is not None:
            queryset = queryset.filter(category=category)

        if category_type is not None:
            queryset = queryset.filter(category_type=category_type)
        
        return queryset



class BrandViewAPI(viewsets.ModelViewSet):
    queryset = Brand.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BrandDetailSerializer
        return BrandSerializer

    def get_queryset(self):
        queryset = self.queryset
        subcategory = self.request.query_params.get('subcategory')

        if subcategory is not None:
            queryset = queryset.filter(subcategory=subcategory)
        return queryset


class TypeViewAPI(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = TypeSerializer

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset