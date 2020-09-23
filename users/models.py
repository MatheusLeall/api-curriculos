from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo que herda de AbstractUser modelo padrão do Django
class User(AbstractUser):
    email = models.EmailField('e-mail address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(null=True, max_length=15)
    city = models.CharField(null=True, max_length=255)
    estate = models.CharField(null=True, max_length=2)
    country = models.CharField(null=True, max_length=255)
    is_recruiter = models.BooleanField(default=False)
