from django.shortcuts import render, redirect
from django.contrib import auth 
from .forms import LoginForm
from .logic import get_redirect_url


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                redirect_url = get_redirect_url(user)
                return redirect(redirect_url)
            else:
                return render(request, 'login/login.html')

    form = LoginForm()
    return render(request, 'login/login.html', {'form': form})
