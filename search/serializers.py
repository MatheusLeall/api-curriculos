# Django REST Framework
from rest_framework import serializers

# Models
from education.models import Education
from experiences.models import Experience
from extras.models import Extra
from projects.models import Project
from users.models import User

class ExperienceCurriculumSerializer(serializers.ModelSerializer):
    """Experience Curriculum Model Serializer"""

    class Meta:
        model = Experience
        fields = (
            'date_ini',
            'date_end',
            'company',
            'description',
        )

class EducationCurriculumSerializer(serializers.ModelSerializer):
    """Education Curriculum Model Serializer"""

    class Meta:
        model = Education
        fields = (
            'date_ini',
            'date_end',
            'title',
        )


class ExtraCurriculumSerializer(serializers.ModelSerializer):
    """Extras Curriculum Model Serializer"""

    class Meta:
        model = Extra
        fields = (
            'expedition',
            'title',
            'url',
            'description',
        )


class ProjectCurriculumSerializer(serializers.ModelSerializer):
    """Projects Curriculum Model Serializer"""

    class Meta:
        model = Project
        fields = (
            'date',
            'title',
            'url',
            'description',
        )


# A classe CurriculumSerializer se encarregará de exibir
# todos os dados relacionados ao usuário.
class CurriculumSerializer(serializers.ModelSerializer):

    experience = ExperienceCurriculumSerializer(many=True)
    education = EducationCurriculumSerializer(many=True)
    extra_education = ExtraCurriculumSerializer(many=True)
    projects = ProjectCurriculumSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone',
            'city',
            'estate',
            'country',
            'experience',
            'education',
            'extra_education',
            'projects',
        )