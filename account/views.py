from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
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

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             ...
#         else:
#             # Return an 'invalid login' error message.
#             ...
#     else:
#         return render(request, 'login: login', {'form': form})
