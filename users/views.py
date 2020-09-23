# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from .serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer

# Models
from .models import User

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Endpoint para realizar o login de usuário
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'User'  : UserModelSerializer(user).data,
            'Token de acesso' : token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    # Endpoint para criação de um novo usuário
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)