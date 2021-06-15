from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import APIUser, CustomUserViewSet, RegisterView, TokenView, MyTokenObtainPairView


router_v1 = DefaultRouter()
router_v1.register('users', CustomUserViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/users/me/', APIUser.as_view()),
    path('v1/auth/email/', RegisterView.as_view(), name='registration'),
    path('v1/auth/token/', MyTokenObtainPairView.as_view(), name='token'),
]
