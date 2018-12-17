from django.contrib import admin
from .models import Position, ManagerProfile, MedWorkerProfile, PatientProfile

admin.site.register(Position)
admin.site.register(ManagerProfile)
admin.site.register(MedWorkerProfile)
admin.site.register(PatientProfile)
