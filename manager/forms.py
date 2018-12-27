from django import forms
from service.models import PatientProfile, MedWorkerProfile, Ward, Position


class SignUpPatientForm(forms.ModelForm):
    last_name = forms.CharField(label='', max_length=100)
    first_name = forms.CharField(label='', max_length=100)
    birth_date = forms.DateField(label='',
                                 widget=forms.DateInput(
                                     attrs={'type': 'date'}))
    ward = forms.ModelChoiceField(queryset=Ward.objects.all(),
                                  empty_label='Палата',
                                  label='')

    class Meta:
        model = PatientProfile
        fields = ['last_name', 'first_name', 'middle_name',
                  'birth_date', 'address', 'contact_phone', 'ward']


class SignUpMedWorkerForm(forms.ModelForm):
    last_name = forms.CharField(label='', max_length=100)
    first_name = forms.CharField(label='', max_length=100)
    position = forms.ModelChoiceField(queryset=Position.objects.all(),
                                      empty_label='Должность',
                                      label='')

    class Meta:
        model = MedWorkerProfile
        fields = ['last_name', 'first_name', 'middle_name',
                  'position']
