from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='')
def home(request):
    user = request.user
    if user.groups.filter(name='manager').exists():
        return redirect('manager:home')
    elif user.groups.filter(name='patient').exists():
        return redirect('/service/')
    elif user.groups.filter(name='medworker').exists():
        return redirect('/service/medworker/')
    return HttpResponse("User don't have any role")


@login_required(redirect_field_name='')
def logout_view(request):
    logout(request)
    return redirect('account:login')
