from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from authen.models import *
from authen.serializers import *
import razorpay
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


PUBLIC_KEY = os.environ.get('RAZORPAY_PUBLIC_KEY')
SECRET_KEY = os.environ.get('RAZORPAY_SECRET_KEY')

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

class AvailableCouponListViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Coupon.objects.filter(active=True).exclude(users=user_id)
        return queryset
    
class FetchCouponViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    def get_queryset(self):
        coupon = self.request.query_params.get('coupon')
        user_id = self.request.query_params.get('user_id')
        queryset = Coupon.objects.filter(code=coupon).exclude(users=user_id)
        return queryset

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
    
@api_view(['POST'])
def start_payment(request):
    # request.data is coming from frontend
    order_id = request.query_params.get('order_id')
    amount = request.query_params.get('amount')

    # setup razorpay client this is the client to whome user is paying money that's you
    client = razorpay.Client(auth=(PUBLIC_KEY, SECRET_KEY))

    # create razorpay order
    # the amount will come in 'paise' that means if we pass 50 amount will become
    # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
    # mumtiply it by 100 so it will be 50 rupees.
    payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})

    # we are saving an order with isPaid=False because we've just initialized the order
    # we haven't received the money we will handle the payment succes in next 
    # function
    payment_data = Payment.objects.create(
                                 order = order_id,
                                 order_payment_id=payment['id'])

    serializer = PaymentSerializer(payment_data)

    """order response will be 
    {'id': 17, 
    'order_date': '23 January 2021 03:28 PM', 
    'order_product': '**product name from frontend**', 
    'order_amount': '**product amount from frontend**', 
    'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
    'isPaid': False}"""

    data = {
        "payment": payment_data,
        "payment_data": serializer.data
    }
    return Response(data)


@api_view(['POST'])
def handle_payment_success(request):
    # request.data is coming from frontend
    res = json.loads(request.data["response"])

    """res will be:
    {'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
    'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
    'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
    this will come from frontend which we will use to validate and confirm the payment
    """

    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    # get order by payment_id which we've created earlier with isPaid=False
    payment = Payment.objects.get(order_payment_id=ord_id)
    order = Order.objects.get(id=payment.order)

    # we will pass this whole data in razorpay client to verify the payment
    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=(PUBLIC_KEY, SECRET_KEY))

    # checking if the transaction is valid or not by passing above data dictionary in 
    # razorpay client if it is "valid" then check will return None
    check = client.utility.verify_payment_signature(data)

    if check is not None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    payment.complete = True
    payment.save()

    # we will turn isPaid=True in order as well
    order.paid = True
    order.save()


    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)