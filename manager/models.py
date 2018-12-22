from django.contrib.auth.models import User
from django.db import models


class ManagerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    mid_name = models.CharField(max_length=100, verbose_name="Фамилия")
