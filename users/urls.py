from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet, RegisterView, TokenView

router_v1 = DefaultRouter()
router_v1.register('users', CustomUserViewSet, basename='user_api')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/email/', RegisterView.as_view(), name='registration'),
    path('v1/auth/token/', TokenView.as_view(), name='token'),
]
