from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view

from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from users.models import CustomUser
from users.utils import get_random_code, get_tokens_for_user, send_mail_to_user

from api.permissions import IsAdmin
from .serializers import CustomUserSerializer, SafeCustomUserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', ]


class APIUser(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = get_object_or_404(CustomUser, id=request.user.id)
            serializer = CustomUserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        user = get_object_or_404(CustomUser, id=request.user.id)
        if request.user == user:
            serializer = SafeCustomUserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        check = CustomUser.objects.filter(email=email).exists()
        if not check:
            confirmation_code = get_random_code(10)
            CustomUser.objects.create_user(email=email, confirmation_code=confirmation_code)
        user = CustomUser.objects.get(email=email)
        confirmation_code = user.confirmation_code
        send_mail_to_user(email, confirmation_code)
        return Response({"email": email, "confirmation_code": confirmation_code})


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = get_object_or_404(CustomUser, email=request.data.get('email'))
        if user.confirmation_code != request.data.get('confirmation_code'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        response = get_tokens_for_user(user)
        return Response(response, status=status.HTTP_200_OK)


# class TokenView(APIView):
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         user = get_object_or_404(CustomUser, email=request.data.get('email'))
#         if user.confirmation_code != request.data.get('confirmation_code'):
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         refresh = RefreshToken.for_user(user)
#         response ={'token': str(refresh.access_token),}
#         return Response(response, status=status.HTTP_200_OK)
#         # token = AccessToken.for_user(user)
#         # response = {'token': {token}}
#         # return Response(response, status=status.HTTP_200_OK)
