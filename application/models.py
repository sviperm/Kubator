from django.db import models

from patient.models import Patient
from med_worker.models import MedWorker
from service.models import Service
# Create your models here.


class ApplicationStatus(models.Model):
    status = models.CharField(max_length=30, verbose_name='Наименование статуса')
    is_application_done = models.BooleanField(verbose_name='Заявка закрыта', default=False)

    def __str__(self):
        return self.status


class ApplicationArchive(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    med_worker = models.ForeignKey(MedWorker, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(ApplicationStatus, on_delete=models.DO_NOTHING)
