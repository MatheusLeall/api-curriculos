# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import SearchViewSet

router = DefaultRouter()
router.register('search', SearchViewSet, basename='search')

urlpatterns = [
    path('', include(router.urls))
]