from django.contrib.auth.models import User
from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100, verbose_name="Должность")

    def __str__(self):
        return self.title


class ManagerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=100, verbose_name="Фамилия")


class MedWorkerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=100, verbose_name="Отчество")
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        verbose_name='Должность'
    )


class PatientProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=100, verbose_name="Отчество")
    birth_date = models.DateField(null=False, verbose_name="Дата рождения")
    address = models.TextField(verbose_name="Адрес")
    contact_phone = models.CharField(max_length=16,
                                     verbose_name="Контактный телефон")
