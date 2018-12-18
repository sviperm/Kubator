from django.urls import path
from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up-patient/', views.signup_patient, name='signup_patient'),
    path('sign-up-medworker/', views.signup_medworker, name='signup_medworker'),
]
