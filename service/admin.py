from django.contrib import admin
from . models import TypeService, Service

# Register your models here.


@admin.register(TypeService)
class TypeServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
