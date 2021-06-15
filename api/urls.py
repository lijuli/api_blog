from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import APIUser, CustomUserViewSet, RegisterView, TokenView, MyTokenObtainPairView


router_v1 = DefaultRouter()


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
