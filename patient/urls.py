from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.get_service_list),
    path('escort/', views.escort),
    path('child/', views.care_child),
    path('food/', views.get_food),
    path('fun/', views.fun),

]
