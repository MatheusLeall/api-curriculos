# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import ProjectViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls))
]