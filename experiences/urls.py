# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import ExperienceViewSet

router = DefaultRouter()
router.register('experiences', ExperienceViewSet, basename='experiences')

urlpatterns = [
    path('', include(router.urls))
]