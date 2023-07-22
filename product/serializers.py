from rest_framework import serializers
from .models import *
from category.serializers import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class HomeBannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBannerImage
        fields = '__all__'
