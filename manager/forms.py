from django import forms
from django.contrib.auth.models import User
from .models import PatientProfile


class SignUpPatientForm(forms.ModelForm):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)
    birth_date = forms.DateField(label='Дата рождения',
                                 widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientProfile
        fields = ['username', 'password', 'last_name', 'first_name', 'mid_name',
                  'birth_date', 'address', 'contact_phone']
