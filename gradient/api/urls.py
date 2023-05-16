from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ActorsViewSet

app_name = 'api'

router = DefaultRouter()
router.register('actors', ActorsViewSet, basename='actors')


urlpatterns = [
    path('', include(router.urls)),
]
