"""Extras URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import ExtraViewSet

router = DefaultRouter()
router.register('extras', ExtraViewSet, basename='extras')

urlpatterns = [
    path('', include(router.urls))
]