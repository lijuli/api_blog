from django.db.models import Max
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.permissions import IsAdminAndAuthenticated
from users.models import CustomUser
from users.utils import get_tokens_for_user, send_mail_to_user

from .serializers import CustomUserSerializer


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
                instance=request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(request.user, many=False)
            return Response(serializer.data)


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
        return Response(
            {"email": email, "confirmation_code": confirmation_code}
        )


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = get_object_or_404(CustomUser, email=request.data.get('email'))
        if user.confirmation_code != request.data.get('confirmation_code'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        response = get_tokens_for_user(user)
        return Response(response, status=status.HTTP_200_OK)
