from django.contrib import admin
from .models import ManagerProfile
from med_worker.models import MedWorkerProfile, Position
from patient.models import PatientProfile

admin.site.register(Position)
admin.site.register(ManagerProfile)
admin.site.register(MedWorkerProfile)
admin.site.register(PatientProfile)
