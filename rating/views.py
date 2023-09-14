from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class RatingViewAPI(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = self.queryset
        product_id = self.request.query_params.get('product_id')
        user_id = self.request.query_params.get('user_id')

        if product_id:
            queryset = queryset.filter(product = product_id)

        if user_id:
            queryset = queryset.filter(user = user_id)
        
        return queryset