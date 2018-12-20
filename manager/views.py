from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import SignUpPatientForm, SignUpMedWorkerForm
from django.contrib.auth.models import Group


def index(request):
    return HttpResponse('hello')


def signup(request, profile):
    # TODO: errors
    if request.method == 'POST':
        if profile == 'patient':
            form = SignUpPatientForm(request.POST)
        elif profile == 'medworker':
            form = SignUpMedWorkerForm(request.POST)
        # TODO: else:
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data['password']
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            group = Group.objects.get(name=profile)
            group.user_set.add(user)
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponse(profile)
    else:
        if profile == 'patient':
            form = SignUpPatientForm()
        elif profile == 'medworker':
            form = SignUpMedWorkerForm()
        # TODO: else:
    return render(request, 'manager/sign_up.html', {'form': form})
