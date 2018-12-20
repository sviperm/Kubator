from django.contrib import admin
from .models import OrderStatus, Order
# Register your models here.


@admin.register(OrderStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class ApplicationArchiveAdmin(admin.ModelAdmin):
    pass
