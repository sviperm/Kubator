from django.urls import path
from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.index, name='home'),
    path('sign-up/<str:profile>/', views.signup, name='signup'),
]
