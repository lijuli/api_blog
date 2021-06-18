from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import api_view
from django.db.models import Avg, Max

from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.decorators import action

from users.models import CustomUser
from users.utils import get_random_code, get_tokens_for_user, send_mail_to_user

from api.permissions import IsAdmin
from .serializers import CustomUserSerializer, SafeCustomUserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdmin]
    pagination_class = PageNumberPagination
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', ]

    @action(detail=False, permission_classes=(IsAuthenticated,),
            methods=['get', 'patch'], url_path='me')
    def get_or_update_self(self, request):
        if request.method != 'GET':
            serializer = self.get_serializer(
                instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(request.user, many=False)
            return Response(serializer.data)




# class APIUser(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = CustomUserSerializer(request.user, many=False)
#         return Response(serializer.data)

#     def patch(self, request):
#         user = get_object_or_404(CustomUser, id=request.user.id)
#         if request.user == user:
#             serializer = SafeCustomUserSerializer(user, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        check = CustomUser.objects.filter(email=email).exists()
        if not check:
            id = CustomUser.objects.aggregate(Max('id'))['id__max'] + 1
            CustomUser.objects.create_user(email=email, username=f'user_{id}')
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

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer