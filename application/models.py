from django.db import models

from patient.models import PatientProfile
from med_worker.models import MedWorkerProfile
from service.models import Service
# Create your models here.


class ApplicationStatus(models.Model):
    status = models.CharField(max_length=30, verbose_name='Наименование статуса')
    is_application_done = models.BooleanField(verbose_name='Заявка закрыта', default=False)

    def __str__(self):
        return self.status


class ApplicationArchive(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.DO_NOTHING)
    med_worker = models.ForeignKey(MedWorkerProfile, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(ApplicationStatus, on_delete=models.DO_NOTHING)

    opening_date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                        blank=True, null=True,
                                        verbose_name='Дата открытия заявки')

    closing_date = models.DateTimeField(auto_now_add=False, auto_now=True,
                                        blank=True, null=True,
                                        verbose_name='Дата закрытия заявки')
