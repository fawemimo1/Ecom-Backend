from django.shortcuts import render
from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
# Create your views here.

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartFetchAPIView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Cart.objects.filter(user=user_id, clear=False, deleted=False)
        return queryset