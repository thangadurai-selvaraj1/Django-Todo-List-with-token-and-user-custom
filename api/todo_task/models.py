from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Task(models.Model):

    PRIORITY = (('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH'))
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    priority = models.CharField(max_length=10, choices=PRIORITY)

    def __str__(self):
        return str(f'{self.owner} ') + str(self.task_name)
