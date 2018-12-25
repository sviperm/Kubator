from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import SignUpPatientForm, SignUpMedWorkerForm
from .helpers import gen_username, is_manager
from django.http import Http404


@login_required(redirect_field_name='')
@user_passes_test(is_manager, redirect_field_name='')
def index(request):
    # TODO: orders in tabs, close order
    return HttpResponse('Manager page')


@login_required(redirect_field_name='')
@user_passes_test(is_manager, redirect_field_name='')
def signup(request, profile):
    if request.method == 'POST':
        if profile == 'patient':
            form = SignUpPatientForm(request.POST)
        elif profile == 'medworker':
            form = SignUpMedWorkerForm(request.POST)
        if form.is_valid():
            user = User()
            username = gen_username(profile)
            user.username = username
            password = User.objects.make_random_password(length=8)
            user.set_password(password)
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            group = Group.objects.get(name=profile)
            group.user_set.add(user)
            profile = form.save(commit=False)
            profile.user = user
            profile.raw_password = password
            profile.save()
            # Get last created object
            # https://docs.djangoproject.com/en/2.1/ref/models/querysets/#latest
            return HttpResponse(f'Login: {username} Password: {password}')
    else:
        if profile == 'patient':
            form = SignUpPatientForm()
        elif profile == 'medworker':
            form = SignUpMedWorkerForm()
        else:
            raise Http404()
    return render(request, 'manager/sign_up.html', {'form': form})
