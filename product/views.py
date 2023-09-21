from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.db.models import Q

class ProductViewAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductDetailSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer

    def get_queryset(self):
        queryset = self.queryset
        category = self.request.query_params.get('category')
        subcategory = self.request.query_params.get('subcategory')
        brand = self.request.query_params.get('brand')
        category_type = self.request.query_params.get('category_type')
        home = self.request.query_params.get('home')

        if category is not None:
            queryset = queryset.filter(category=category)

        if subcategory is not None:
            queryset = queryset.filter(subcategory=subcategory)

        if brand is not None:
            queryset = queryset.filter(brand=brand)

        if category_type is not None:
            queryset = queryset.filter(category_type=category_type)
        
        if home is not None:
            queryset = queryset.filter(home_product=True)
        
        return queryset

class ProductImageViewAPI(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        queryset = self.queryset
        product = self.request.query_params.get('product')
        if product is not None:
            queryset = queryset.filter(product=product)
        return queryset


class ImageViewAPI(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class PictureAPIView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


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
            Q(subcategory__name__icontains=keyword) |
            Q(brand__name__icontains=keyword) |
            Q(gender__icontains=keyword)

        )
        return queryset


class HomeBannerImageAPIView(viewsets.ModelViewSet):
    serializer_class = HomeBannerImageSerializer

    def get_queryset(self):
        queryset = HomeBannerImage.objects.all()
        filter = self.request.query_params.get('filter')

        if filter:
            queryset = HomeBannerImage.objects.filter(visibility=True)
        return queryset

    def partial_update(self, request, pk):
        try:
            banner = HomeBannerImage.objects.get(pk=pk)
            visibility = request.data.get('visibility', False)  # Get the new visibility value from request data

            # Set visibility to False for all other banners
            HomeBannerImage.objects.exclude(pk=pk).update(visibility=False)

            banner.visibility = visibility  # Set the visibility for the specific banner
            banner.save()

            serializer = HomeBannerImageSerializer(banner)
            return Response(serializer.data)
        except HomeBannerImage.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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