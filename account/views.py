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
        # TODO: set url
        return redirect('/admin/')
    elif user.groups.filter(name='medworker').exists():
        # TODO: set urls
        return redirect('/admin/')
    return HttpResponse("User don't have any role")


@login_required(redirect_field_name='')
def logout_view(request):
    logout(request)
    return redirect('account:login')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('account:home')
#         else:
#             return render(request, 'registrations/login.html', {'error': True})
#     return render(request, 'registrations/login.html')
