# from django.shortcuts import render
# from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home page')

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