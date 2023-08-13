from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.db.models import Q

class ProductViewAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewAPI(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductDetailViewAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ImageViewAPI(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class HomeProductDetailViewAPI(viewsets.ModelViewSet):
    queryset = Product.objects.filter(home_product=True)
    serializer_class = ProductDetailSerializer

class PictureAPIView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class ImageFetchAPIView(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer
    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        queryset = ProductImage.objects.filter(product=product_id)
        return queryset

class ColorImageFetchAPIView(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        queryset = Image.objects.filter(product=product_id)
        return queryset


class SearchAPIView(viewsets.ModelViewSet):
    serializer_class = ProductDetailSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        queryset = Product.objects.filter(
            Q(name__icontains=keyword) |
            Q(description__icontains=keyword) |
            Q(category__name__icontains=keyword) |
            Q(brand__name__icontains=keyword) |
            Q(gender__icontains=keyword)

        )
        return queryset

class CategoryProductFetchAPIView(viewsets.ModelViewSet):
    serializer_class = ProductDetailSerializer
    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        queryset = Product.objects.filter(category=category_id)
        return queryset

class HomeBannerImageAPIView(viewsets.ModelViewSet):
    serializer_class = HomeBannerImageSerializer
    def get_queryset(self):
        queryset = HomeBannerImage.objects.all()
        return queryset

class SizeAPIView(viewsets.ModelViewSet):
    serializer_class = SizeSerializer
    def get_queryset(self):
        queryset = Size.objects.all()
        return queryset


class ColorAPIView(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    def get_queryset(self):
        queryset = Color.objects.all()
        return queryset