# Django REST Framework
from rest_framework import serializers

# Models
from .models import Experience


# Classe de serialização do modelo Experience
class ExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            'pk',
            'date_ini',
            'date_end',
            'company',
            'description',
        )


class ExperienceSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_ini = serializers.DateTimeField()
    date_end = serializers.DateTimeField(required=False)
    company = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=10000)

    def create(self, data):
        exp = Experience.objects.create(**data)
        return exp