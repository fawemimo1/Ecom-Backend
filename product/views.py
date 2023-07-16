from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


class ProductViewAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewAPI(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductDetailViewAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ImageFetchAPIView(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        queryset = ProductImage.objects.filter(product=product_id)
        return queryset
    
class CategoryProductFetchAPIView(viewsets.ModelViewSet):
    serializer_class = ProductDetailSerializer
    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        queryset = ProductImage.objects.filter(product=category_id)
        return queryset