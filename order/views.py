from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from authen.models import *
from authen.serializers import *


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class CouponListViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.filter(active=True)
    serializer_class = CouponSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class OrderFetchAPIView(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Order.objects.filter(user=user_id)
        return queryset

class ProfileFetchAPIView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Profile.objects.filter(user=user_id)
        return queryset

class AddressFetchAPIView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Address.objects.filter(user=user_id)
        return queryset