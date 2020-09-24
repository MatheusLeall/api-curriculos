from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('experiences.urls', 'experiences'), namespace='experiences')),
    path('', include(('education.urls', 'education'), namespace='education')),
    path('', include(('projects.urls', 'projects'), namespace='projects')),
    path('', include(('extras.urls', 'extras'), namespace='extras')),
    path('', include(('search.urls', 'search'), namespace='search')),
]
