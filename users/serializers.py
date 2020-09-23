# Django
from django.contrib.auth import password_validation, authenticate

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from .models import User

# Biblioteca para validar expressões regulares do Django
from django.core.validators import RegexValidator


# Classe para serializar os dados do usuário
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

# Classe para realizar o login do usuário
class UserLoginSerializer(serializers.Serializer):

    # Campos que serão obrigatórios para login do usuário
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    # Método para validação dos dados de login (email e senha)
    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('E-mail e/ou senha incorretos!')
    
        self.context['user'] = user
        return data

    # Método que cria ou recebe um token já existente para o usuário
    def create(self, data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

# Classe para realizar cadastro de novo usuário
class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    city = serializers.CharField(max_length=255, required=False)
    estate = serializers.CharField(max_length=2, required=False)
    country = serializers.CharField(max_length=255, required=False)
    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = 'Informe um número de telefone válido'
    )
    phone = serializers.CharField(validators=[phone_regex], required=False)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)

    # Método que realiza a validaçã dos dados neste caso somente a validação da senha
    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError('As senhas informadas não coincidem!')

        password_validation.validate_password(passwd)

        return data

    # Método para criar o novo usuário
    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        return user