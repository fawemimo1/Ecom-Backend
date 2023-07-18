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
        queryset = Product.objects.filter(category=category_id)
        return queryset
    
class HomeProductAPIView(viewsets.ModelViewSet):
    serializer_class = HomeProductSerializer
    def get_queryset(self):
        queryset = HomeProduct.objects.all()
        return queryset
    
class NewProductAPIView(viewsets.ModelViewSet):
    serializer_class = NewProductSerializer
    def get_queryset(self):
        queryset = NewProduct.objects.all()
        return queryset
    
class TopProductAPIView(viewsets.ModelViewSet):
    serializer_class = TopProductSerializer
    def get_queryset(self):
        queryset = TopProduct.objects.all()
        return queryset
    
class HomeProductDetailAPIView(viewsets.ModelViewSet):
    serializer_class = HomeProductDetailSerializer
    def get_queryset(self):
        queryset = HomeProduct.objects.all()
        return queryset
    
class NewProductDetailAPIView(viewsets.ModelViewSet):
    serializer_class = NewProductDetailSerializer
    def get_queryset(self):
        queryset = NewProduct.objects.all()
        return queryset
    
class TopProductDetailAPIView(viewsets.ModelViewSet):
    serializer_class = TopProductDetailSerializer
    def get_queryset(self):
        queryset = TopProduct.objects.all()
        return queryset
    
class NewProductImageAPIView(viewsets.ModelViewSet):
    serializer_class = NewProductImageSerializer
    def get_queryset(self):
        queryset = NewProductImage.objects.all()
        return queryset
    
class HomeProductImageAPIView(viewsets.ModelViewSet):
    serializer_class = HomeProductImageSerializer
    def get_queryset(self):
        queryset = HomeProductImage.objects.all()
        return queryset
    
class TopProductImageAPIView(viewsets.ModelViewSet):
    serializer_class = TopProductImageSerializer
    def get_queryset(self):
        queryset = TopProductImage.objects.all()
        return queryset
    
class HomeBannerImageAPIView(viewsets.ModelViewSet):
    serializer_class = HomeBannerImageSerializer
    def get_queryset(self):
        queryset = HomeBannerImage.objects.all()
        return queryset
    
class HomeImageFetchAPIView(viewsets.ModelViewSet):
    serializer_class = HomeProductImageSerializer
    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        queryset = HomeProductImage.objects.filter(product=product_id)
        return queryset

class NewImageFetchAPIView(viewsets.ModelViewSet):
    serializer_class = NewProductImageSerializer
    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        queryset = NewProductImage.objects.filter(product=product_id)
        return queryset
    
class TopImageFetchAPIView(viewsets.ModelViewSet):
    serializer_class = TopProductImageSerializer
    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        queryset = TopProductImage.objects.filter(product=product_id)
        return queryset
    
