from django.db import models
from patient.models import Patient


# Create your models here.
class TypeService(models.Model):
    type = models.CharField(max_length=120, verbose_name="Тип услуги")


class Service(models.Model):
    name = models.CharField(max_length=120, verbose_name="Наименование услуги")
    type = models.ForeignKey(TypeService, on_delete=models.DO_NOTHING)
