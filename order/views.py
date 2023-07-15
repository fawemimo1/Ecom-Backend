from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

class OrderFetchAPIView(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Order.objects.filter(user=user_id)
        return queryset