from django.contrib import admin

from .models import MedWorkerProfile, Position, PatientProfile, Order, OrderStatus, Service

admin.site.register(Position)
admin.site.register(MedWorkerProfile)
admin.site.register(PatientProfile)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Service)

# from . models import Service  # ,TypeService

# Register your models here.


# @admin.register(TypeService)
# class TypeServiceAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     pass
