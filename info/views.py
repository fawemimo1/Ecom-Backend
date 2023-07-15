from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from .models import StoreInfo
from .serializers import StoreInfoSerializer

class StoreInfoViewSet(viewsets.ModelViewSet):
    queryset = StoreInfo.objects.all()
    serializer_class = StoreInfoSerializer
