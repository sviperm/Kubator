from django import forms
from django.contrib.auth.models import User
from service.models import PatientProfile, MedWorkerProfile


class SignUpPatientForm(forms.ModelForm):
    last_name = forms.CharField(label='Фамилия', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)
    birth_date = forms.DateField(label='Дата рождения',
                                 widget=forms.DateInput(
                                     attrs={'type': 'date'}))

    class Meta:
        model = PatientProfile
        fields = ['last_name', 'first_name', 'middle_name',
                  'birth_date', 'address', 'contact_phone']


class SignUpMedWorkerForm(forms.ModelForm):
    last_name = forms.CharField(label='Фамилия', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)

    class Meta:
        model = MedWorkerProfile
        fields = ['last_name', 'first_name', 'middle_name',
                  'position']
