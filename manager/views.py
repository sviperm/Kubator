from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpPatientForm


def index(request):
    return HttpResponse('hello')


def signup(request):
    if request.method == 'POST':
        form = SignUpPatientForm(request.POST)
        if form.is_valid():
            # user = User()
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.save()
            # raw_password = form.cleaned_data.get('password')
            return HttpResponse(form.cleaned_data['username'])
    else:
        form = SignUpPatientForm()
    return render(request, 'manager/sign_up.html', {'form': form})
