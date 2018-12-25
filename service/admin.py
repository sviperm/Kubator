from django.contrib import admin
from .models import MedWorkerProfile, Position, PatientProfile, Order, OrderStatus, Service

admin.site.register(Position)
admin.site.register(MedWorkerProfile)
admin.site.register(PatientProfile)
admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Service)
