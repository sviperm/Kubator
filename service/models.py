from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    title = models.CharField(
        max_length=100, unique=True, verbose_name="Должность")

    def __str__(self):
        return self.title


class MedWorkerProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    raw_password = models.CharField(max_length=8, verbose_name="Пароль")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    position = models.ForeignKey(
        'Position',
        on_delete=models.CASCADE,
        verbose_name='Должность'
    )

    def __str__(self):
        return f'{self.user.username} {self.raw_password} {self.user.last_name} {self.user.first_name} {self.middle_name}: {self.position}'


class Ward(models.Model):
    number = models.CharField(max_length=2, verbose_name='Номер палаты')


class PatientProfile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    raw_password = models.CharField(max_length=8, verbose_name="Пароль")
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, verbose_name="Номер палаты")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    birth_date = models.DateField(null=False, verbose_name="Дата рождения")
    address = models.TextField(verbose_name="Адрес")
    contact_phone = models.CharField(max_length=16,
                                     verbose_name="Контактный телефон")

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class Service(models.Model):
    name = models.CharField(max_length=120, verbose_name="Наименование услуги")

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    name = models.CharField(max_length=20, unique=True,
                            verbose_name='Наименование статуса')
    done = models.BooleanField(verbose_name='Заявка закрыта', default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    worker = models.ForeignKey(MedWorkerProfile, on_delete=models.CASCADE,
                               blank=True, null=True)

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    report = models.TextField(blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                         verbose_name='Дата поступления заявки')

    opening_date = models.DateTimeField(auto_now_add=False, auto_now=False,
                                        blank=True, null=True,
                                        verbose_name='Дата открытия заявки')

    closing_date = models.DateTimeField(auto_now_add=False, auto_now=False,
                                        blank=True, null=True,
                                        verbose_name='Дата закрытия заявки')

    def __str__(self):
        return f"{self.patient.user.username} {self.service.name}"
