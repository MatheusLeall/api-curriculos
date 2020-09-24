from django.db import models
from users.models import User

from ckeditor.fields import RichTextField

class Extra(models.Model):
    """ Modelo de formações extra-curriculares """

    user = models.ForeignKey(
           User, 
           on_delete=models.CASCADE,
           related_name='extra_education'
         )
    expedition = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    description = RichTextField(null=True)


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'
