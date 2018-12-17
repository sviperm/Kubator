from django.contrib.auth.models import User
from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100, verbose_name="Должность")


class ManagerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)


class MedWorkerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=100, verbose_name="Фамилия")
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
    )


class PatientProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=100, verbose_name="Отчество")
    birth_date = models.DateField(null=False, verbose_name="Дата рождения")
    address = models.TextField(verbose_name="Адрес")
    contact_phone = models.CharField(max_length=16,
                                     verbose_name="Контактный телефон")
