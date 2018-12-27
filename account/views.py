from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from manager.helpers import is_manager, is_medworker, is_patient


def error_404_view(request, exception):
    return render(request, '404.html')


def home(request):
    user = request.user
    if is_manager(user):
        return redirect('manager:home')
    elif is_patient(user):
        return redirect('service/patient/')
    elif is_medworker(user):
        return redirect('service/medworker/')
    else:
        return redirect('account:login')


@login_required(redirect_field_name='')
def logout_view(request):
    logout(request)
    return redirect('account:login')
