# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import EducationViewSet

router = DefaultRouter()
router.register('education', EducationViewSet, basename='education')

urlpatterns = [
    path('', include(router.urls))
]