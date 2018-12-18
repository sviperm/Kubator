from django.shortcuts import render, redirect
# from .models import Service
from . import forms
# from . logic import check_user


# def simulator():
#     pass


###############################################################################
def get_service_list(request):
    return render(request, 'service/service_list.html', forms.ContextServiceList)


###############################################################################
def get_food_list(request):
    return render(request, 'service/food_list.html', forms.ContextFoodList)


def get_eating(request):
    # user = check_user(request.user)
    # if user:
    #     user_id = user.id
    #     service_id = Service.objects.get(name__iexact="Принести еду").id

    return redirect('service_list')


def get_drinking(request):
    return redirect('service_list')


###############################################################################
def get_baby_list(request):
    return render(request, 'service/baby_list.html', forms.ContextBabyList)


def bring_baby(request):
    return redirect('service_list')


def carry_out_baby(request):
    return redirect('service_list')


###############################################################################
def get_escort_list(request):
    return render(request, 'service/escort_list.html', forms.ContextEscortList)


def escort_to_wc(request):
    return redirect('service_list')


def escort_to_wash(request):
    return redirect('service_list')


def escort_to_procedure(request):
    return redirect('service_list')


###############################################################################
def alert(request):
    return redirect('service_list')


###############################################################################
def fun(request):
    return redirect('service_list')


###############################################################################
def get_archive(request):
    return redirect('service_list')
