# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from .models import User

class IsStandardUser(BasePermission):
    """ Permite acesso para adicionar experiencias, escolaridade e projetos """

    def has_permission(self, request, view):
        try:
            user = User.objects.get(email=request.user, is_recruiter=False)
        except User.DoesNotExist:
            return False
        return True