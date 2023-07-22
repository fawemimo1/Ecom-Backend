from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
import requests

# from django.contrib.auth import get_user_model
# User = get_user_model()

import random

def generate_4_digit_code():
    return random.randint(1000, 9999)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserViewAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LogoutAndBlacklistRefreshToken(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        id = self.kwargs['id']
        obj = User.objects.get(id=id)
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileViewAPI(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class SendSMS(APIView):
    def post(self, request, format=None):
        url = "https://www.fast2sms.com/dev/bulkV2"
        numbers = request.data.get('numbers', '')  # Get the numbers from POST data
        code = generate_4_digit_code()
        if not numbers:
            return Response({"error": "Phone numbers are required."}, status=status.HTTP_400_BAD_REQUEST)

        payload = f"variables_values={code}&route=otp&numbers={numbers}"
        headers = {
            'authorization': "rA1utghpRkIlz7thMPOJkYvYRd3pIDMhoMebNtEn2ggOnnKbMMlQaWGXWnj2",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
        }

        try:
            response = requests.post(url, data=payload, headers=headers)
            response_data = response.json()

            # Pass the generated code to the frontend in the response data
            response_data['code'] = code

            # Save the response data to the SMS model or process it as required
            # Example: 
            # sms = SMS.objects.create(data=response_data)

            return Response(response_data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            error_msg = {"error": "Failed to send SMS. Error: {}".format(str(e))}
            return Response(error_msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
