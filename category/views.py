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

class SubCategoryCategoryFetchAPIView(viewsets.ModelViewSet):
    serializer_class = SubCategoryDetailSerializer
    def get_queryset(self):
        cat_id = self.request.query_params.get('cat_id')
        queryset = SubCategory.objects.filter(category =  cat_id)
        return queryset
    
class BrandSubCategoryFetchAPIView(viewsets.ModelViewSet):
    serializer_class = BrandDetailSerializer
    def get_queryset(self):
        subcat_id = self.request.query_params.get('subcat_id')
        queryset = Brand.objects.filter(subcategory =  subcat_id)
        return queryset

class BrandViewAPI(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandDetailViewAPI(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer