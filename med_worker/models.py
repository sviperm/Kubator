from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.title


class MedWorkerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, verbose_name="Отчество", blank=True, null=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE, verbose_name='Должность')
