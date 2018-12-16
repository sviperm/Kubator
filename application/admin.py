from django.contrib import admin
from .models import ApplicationStatus, ApplicationArchive
# Register your models here.


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(ApplicationArchive)
class ApplicationArchiveAdmin(admin.ModelAdmin):
    pass
