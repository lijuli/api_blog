from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


router_v1 = DefaultRouter()


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/email/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1//auth/token/', TokenRefreshView.as_view(), name='token_refresh'),
]
