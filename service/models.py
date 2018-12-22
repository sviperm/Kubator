from django.db import models


# class TypeService(models.Model):
#     type = models.CharField(max_length=120, verbose_name="Наименование типа услуги")
#
#     def __str__(self):
#         return self.type


class Service(models.Model):
    name = models.CharField(max_length=120, verbose_name="Наименование услуги")
    # type = models.ForeignKey(TypeService, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
