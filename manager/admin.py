from django.contrib import admin
from .models import ManagerProfile
from service.models import PatientProfile, MedWorkerProfile, Position

admin.site.register(Position)
admin.site.register(ManagerProfile)
admin.site.register(MedWorkerProfile)
admin.site.register(PatientProfile)
