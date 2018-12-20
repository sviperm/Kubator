from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    title = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.title


class MedWorkerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=100, verbose_name="Отчество")
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        verbose_name='Должность'
    )

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.mid_name}: {self.position}'
