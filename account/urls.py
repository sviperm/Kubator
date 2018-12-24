from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    # TODO: custom, login, logout
    path('', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls')),
]
