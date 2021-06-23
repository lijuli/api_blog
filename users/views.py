from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsAdminAndAuthenticated
from users.models import CustomUser
from users.utils import get_tokens_for_user, send_email_to_user

from .serializers import (CustomUserSerializer, RegisterSerializer,
                          TokenSerializer)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'
    permission_classes = [IsAdminAndAuthenticated]
    pagination_class = PageNumberPagination

    @action(detail=False, permission_classes=(IsAuthenticated,),
            methods=['get', 'patch'], url_path='me')
    def get_or_update_self(self, request):
        if request.method != 'GET':
            serializer = self.get_serializer(
                instance=request.user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        serializer = self.get_serializer(request.user, many=False)
        return Response(serializer.data)


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid()
        email = serializer.validated_data['email']
        user = CustomUser.objects.get_or_create(email=email)
        confirmation_code = user[0].confirmation_code
        send_email_to_user(email, confirmation_code)
        return Response(
            {"email": email, "confirmation_code": confirmation_code}
        )


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid()
        email = serializer.validated_data['email']
        confirmation_code = serializer.validated_data['confirmation_code']
        user = get_object_or_404(CustomUser, email=email)
        if str(user.confirmation_code) != confirmation_code:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        response = get_tokens_for_user(user)
        return Response(response, status=status.HTTP_200_OK)
