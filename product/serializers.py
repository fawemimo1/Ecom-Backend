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

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class HomeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = '__all__'

class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProduct
        fields = '__all__'

class TopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProduct
        fields = '__all__'

class HomeProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProduct
        fields = '__all__'
        depth = 1

class NewProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProduct
        fields = '__all__'
        depth = 1

class TopProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProduct
        fields = '__all__'
        depth = 1


class NewProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProductImage
        fields = '__all__'

class HomeProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProductImage
        fields = '__all__'

class TopProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopProductImage
        fields = '__all__'

class HomeBannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBannerImage
        fields = '__all__'