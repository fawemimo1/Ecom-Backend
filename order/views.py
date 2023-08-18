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
from rest_framework import status
from rest_framework.views import APIView
from .constants import PaymentStatus
from django.shortcuts import get_object_or_404
PUBLIC_KEY = os.environ.get('RAZORPAY_PUBLIC_KEY', None)
SECRET_KEY = os.environ.get('RAZORPAY_SECRET_KEY', None)

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
    
# Get Razorpay Key id and secret for authorizing razorpay client.

# Creating a Razorpay Client instance.
razorpay_client = razorpay.Client(auth=("rzp_test_no6wvyoP4nQF2v", "tC4rjsgxUekbQZOPqPVTPocx"))


class PaymentView(APIView):
    """
    APIView for Creating Razorpay Order.
    :return: list of all necessary values to open Razorpay SDK
    """

    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')  # Use request.data instead of query_params for POST requests
        name = request.data.get('name')
        amount = request.data.get('amount')

        # Create Order
        razorpay_order = razorpay_client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )

        # Save the order in DB
        order = Payment.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order["id"],
            order_id=order_id,  # Use the provided order_id here
            status='Pending',
        )

        data = {
            "name": name,
            "merchantId": "RAZOR_KEY",
            "amount": amount,
            "currency": 'INR',
            "orderId": razorpay_order["id"],
        }

        # Save order details to frontend
        return Response(data, status=status.HTTP_200_OK)

class CallbackView(APIView):
    
    """
    APIView for Verifying Razorpay Order.
    :return: Success and failure response messages
    """

    @staticmethod
    def post(request, *args, **kwargs):

        # getting data form request
        response = request.data.dict()

        """
            if razorpay_signature is present in the request 
            it will try to verify
            else throw error_reason
        """
        if "razorpay_signature" in response:

            # Verifying Payment Signature
            data = razorpay_client.utility.verify_payment_signature(response)

            # if we get here True signature
            if data:
                payment_object = get_object_or_404(Payment, provider_order_id=response['razorpay_order_id'])
                order = get_object_or_404(Order, id=payment_object.order.id)  
                order.paid = True         # razorpay_payment = RazorpayPayment.objects.get(order_id=response['razorpay_order_id'])
                payment_object.status = PaymentStatus.SUCCESS
                payment_object.payment_id = response['razorpay_payment_id']
                payment_object.signature_id = response['razorpay_signature']     
                payment_object.complete = True     
                payment_object.save()
                order.save()
                context = {'status': 'Payment Done'}
                return render(request, 'payment_success_template.html', context)
                # return Response({'status': 'Payment Done'}, status=status.HTTP_200_OK)
            else:
                context = {'status': 'Signature Mismatch!'}
                return render(request, 'payment_failure_template.html', context)
                # return Response({'status': 'Signature Mismatch!'}, status=status.HTTP_400_BAD_REQUEST)

        # Handling failed payments
        else:
            error_code = response['error[code]']
            error_description = response['error[description]']
            error_source = response['error[source]']
            error_reason = response['error[reason]']
            error_metadata = json.loads(response['error[metadata]'])
            razorpay_payment =   Payment.objects.get(provider_order_id=error_metadata['order_id'])
            razorpay_payment.payment_id = error_metadata['payment_id']
            razorpay_payment.signature_id = "None"
            razorpay_payment.status = PaymentStatus.FAILURE
            razorpay_payment.save()

            error_status = {
                'error_code': error_code,
                'error_description': error_description,
                'error_source': error_source,
                'error_reason': error_reason,
            }
            context = {'status': error_status}
            return render(request, 'payment_failure_template.html', context)

            # return Response({'error_data': error_status}, status=status.HTTP_401_UNAUTHORIZED)