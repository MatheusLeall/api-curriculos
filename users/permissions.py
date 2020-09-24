# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from .models import User

# Classe de permissão de usuário
class IsStandardUser(BasePermission):
    """ Permite acesso para adicionar experiencias, escolaridade e projetos """

    def has_permission(self, request, view):
        try:
            user = User.objects.get(email=request.user, is_recruiter=False)
        except User.DoesNotExist:
            return False
        return True


# Classe de permissão do recrutador
class IsRecruiterUser(BasePermission):
    """ Permite acesso para buscar currículos """

    def has_permission(self, request, view):
        try:
            user = User.objects.get(email=request.user, is_recruiter=True)
        except User.DoesNotExist:
            return False
        return True