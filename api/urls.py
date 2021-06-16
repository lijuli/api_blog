from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet
from api.views import ReviewViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/titles', TitleViewSet, basename='title_api')
router_v1.register(r'v1/titles/(?P<title_id>[0-9]+)/reviews',
                   ReviewViewSet,
                   basename='reviews_api')

urlpatterns = [
    path('', include(router_v1.urls)),
]
