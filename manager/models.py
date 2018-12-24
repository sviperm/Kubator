from django.db import models
from django.contrib.auth.models import User


class ManagerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
