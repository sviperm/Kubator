from django.db import models
from django.contrib.auth.models import User, BaseUserManager
# Create your models here.
# class Address(models.Model):
#     pass


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=150, verbose_name="Фамилия")
    data_of_birth = models.DateField(verbose_name="Дата рождения")
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address = models.TextField()

    # https://ru.wikipedia.org/wiki/Телефонный_номер
    # 15 знаков на цифры и "+" - префикс
    phone_number = models.CharField(max_length=16, verbose_name="Телефонный номер")
