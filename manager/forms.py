from django import forms
from django.contrib.auth.models import User
from patient.models import PatientProfile
from med_worker.models import MedWorkerProfile


# class SignUpPatientForm(forms.ModelForm):
#     mid_name = forms.CharField(max_length=100,
#                                label='Отчество')
#     birth_date = forms.DateField(label='Дата рождения',
#                                  widget=forms.DateInput(attrs={'type': 'date'}))
#     address = forms.CharField(widget=forms.Textarea(),
#                               label='Адрес')
#     contact_phone = forms.CharField(label='Номер телефона', max_length=15)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'last_name', 'first_name', 'mid_name',
#                   'birth_date', 'address', 'contact_phone']


class SignUpPatientForm(forms.ModelForm):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)
    birth_date = forms.DateField(label='Дата рождения',
                                 widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PatientProfile
        fields = ['username', 'password', 'last_name', 'first_name', 'middle_name',
                  'birth_date', 'address', 'contact_phone']


class SignUpMedWorkerForm(forms.ModelForm):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', max_length=100)
    last_name = forms.CharField(label='Фамилия', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)

    class Meta:
        model = MedWorkerProfile
        fields = ['username', 'password', 'last_name', 'first_name', 'middle_name',
                  'position']
