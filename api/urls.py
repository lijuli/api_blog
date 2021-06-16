from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet
from users.views import CustomUserViewSet, APIUser, RegisterView, MyTokenObtainPairView, TokenView

router_v1 = DefaultRouter()
router_v1.register('v1/titles', TitleViewSet, basename='title_api')
router_v1.register('v1/users', CustomUserViewSet, basename='user_api')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/users/me/', APIUser.as_view(), name='about'),
    path('v1/auth/email/', RegisterView.as_view(), name='registration'),
    path('v1/auth/token/', TokenView.as_view(), name='token'),
]
