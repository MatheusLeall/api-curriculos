# Django REST Framework
from rest_framework import serializers
# Model
from .models import Education

class EducationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'pk',
            'date_ini',
            'date_end',
            'title',
        )

class EducationSerializer(serializers.Serializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_ini = serializers.DateTimeField()
    date_end = serializers.DateTimeField(required=False)
    title = serializers.CharField(max_length=255)

    def create(self, data):

        education = Education.objects.create(**data)
        return education