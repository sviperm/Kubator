from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import SignUpPatientForm, SignUpMedWorkerForm
from .models import ManagerProfile
from .helpers import gen_username, is_manager


@user_passes_test(is_manager, redirect_field_name='', login_url='account:home')
def index(request):
    # TODO: orders in tabs, close order
    if request.method == 'POST':
        if request.POST['redirect'] == 'medworker':
            return redirect('manager:signup', 'medworker')
        elif request.POST['redirect'] == 'patient':
            return redirect('manager:signup', 'patient')
    else:
        middle_name = ManagerProfile.objects.get(
            user=request.user.pk).middle_name
        context = {'last_name': request.user.last_name,
                   'first_name': request.user.first_name,
                   'middle_name': middle_name}
        return render(request, 'manager/manager_cab.html', context)


@user_passes_test(is_manager, redirect_field_name='', login_url='account:home')
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
            context = {'username': username,
                       'password': password}
            return render(request, 'manager/login_password.html', context)
    else:
        if profile == 'patient':
            form = SignUpPatientForm()
            return render(request, 'manager/patient_sign_up.html', {'form': form})
        elif profile == 'medworker':
            form = SignUpMedWorkerForm()
            return render(request, 'manager/medworker_sign_up.html', {'form': form})
        else:
            raise Http404()
    return render(request, 'manager/sign_up.html', {'form': form})
