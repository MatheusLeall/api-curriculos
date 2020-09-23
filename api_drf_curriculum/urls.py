from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('experiences.urls', 'experiences'), namespace='experiences')),
    path('', include(('education.urls', 'education'), namespace='education')),
    path('', include(('projects.urls', 'projects'), namespace='projects')),
    path('', include(('extras.urls', 'extras'), namespace='extras')),
]
