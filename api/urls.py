from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TitleViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/titles', TitleViewSet, basename='title_api')

urlpatterns = [
    path('', include(router_v1.urls)),
]
