from django.db import models
from Kubator.patient.models import Patient


# Create your models here.
class TypeService(models.Model):
    type = models.CharField(max_length=120)


class Service(models.Model):
    name = models.CharField(max_length=120)
    type = models.ForeignKey(TypeService, on_delete=models.DO_NOTHING)
    done = models.BooleanField(default=False)


class ServiceArchive(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
