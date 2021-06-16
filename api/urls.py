from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet
from api.views import ReviewViewSet
from api.views import CategoryViewSet
from api.views import GenreViewSet
from users.views import CustomUserViewSet, APIUser, RegisterView, MyTokenObtainPairView, TokenView

router_v1 = DefaultRouter()
router_v1.register('titles', TitleViewSet, basename='title_api')
router_v1.register(r'titles/(?P<title_id>[0-9]+)/reviews',
                   ReviewViewSet,
                   basename='review_api')
router_v1.register('categories', CategoryViewSet, basename='category_api')
router_v1.register('genres', GenreViewSet, basename='genre_api')
router_v1.register('users', CustomUserViewSet, basename='user_api')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/users/me/', APIUser.as_view(), name='about'),
    path('v1/auth/email/', RegisterView.as_view(), name='registration'),
    path('v1/auth/token/', TokenView.as_view(), name='token'),
]
