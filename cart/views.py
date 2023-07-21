from django.shortcuts import render
from rest_framework import viewsets
from .models import WishList
from .serializers import WishListSerializer
# Create your views here.

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

class WishListFetchAPIView(viewsets.ModelViewSet):
    serializer_class = WishListSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = WishList.objects.filter(user=user_id, clear=False, deleted=False)
        return queryset