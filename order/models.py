from django.db import models

from patient.models import PatientProfile
from med_worker.models import MedWorkerProfile
from service.models import Service
# Create your models here.


class OrderStatus(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Наименование статуса')
    done = models.BooleanField(verbose_name='Заявка закрыта', default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(PatientProfile, on_delete=models.DO_NOTHING)
    worker = models.ForeignKey(MedWorkerProfile, on_delete=models.DO_NOTHING,
                               blank=True, null=True)

    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING)
    report = models.TextField()

    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                         verbose_name='Дата поступления заявки')

    opening_date = models.DateTimeField(auto_now_add=False, auto_now=False,
                                        blank=True, null=True,
                                        verbose_name='Дата открытия заявки')

    closing_date = models.DateTimeField(auto_now_add=False, auto_now=False,
                                        blank=True, null=True,
                                        verbose_name='Дата закрытия заявки')
