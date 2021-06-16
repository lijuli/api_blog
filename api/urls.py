from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet
# from api.views import ReviewViewSet
from api.views import CategoryViewSet
from api.views import GenreViewSet

router_v1 = DefaultRouter()
router_v1.register('titles', TitleViewSet, basename='title_api')
# router_v1.register(r'v1/titles/(?P<title_id>[0-9]+)/reviews',
#                    ReviewViewSet,
#                    basename='review_api')
router_v1.register(r'categories', CategoryViewSet, basename='category_api')
router_v1.register(r'genres', GenreViewSet, basename='genre_api')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
