from rest_framework import serializers
from .models import StoreInfo

class StoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreInfo
        fields = '__all__'