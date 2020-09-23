from django.db import models
from users.models import User

class Education(models.Model):
    """ Modelo de grau de escolaridade """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ini = models.DateTimeField()
    date_end = models.DateTimeField(null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.title}'
