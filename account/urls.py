from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
