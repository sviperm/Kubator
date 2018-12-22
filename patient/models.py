from django.db import models
from django.contrib.auth.models import User


class PatientProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    birth_date = models.DateField(null=False, verbose_name="Дата рождения")
    address = models.TextField(verbose_name="Адрес")
    contact_phone = models.CharField(max_length=16,
                                     verbose_name="Контактный телефон")
