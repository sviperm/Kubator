from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    title = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.title


class MedWorkerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    raw_password = models.CharField(max_length=8, verbose_name="Пароль")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        verbose_name='Должность'
    )

    def __str__(self):
        return f'{self.user.username} {self.raw_password} {self.user.last_name} {self.user.first_name} {self.middle_name}: {self.position}'
