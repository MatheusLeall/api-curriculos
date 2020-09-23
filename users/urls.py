# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]