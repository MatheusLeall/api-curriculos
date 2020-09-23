from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Project(models.Model):
    """ Modelo de projetos """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    description = RichTextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'

