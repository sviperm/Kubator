from django.shortcuts import render, redirect
from .models import Service
from . import forms
from . import logic


# def simulator():
#     pass


def build_service_list(request, template, context):
    user = logic.is_patient(request.user)
    if user:
        return render(request, template, context)
    return redirect(logic.get_redirect_url(user))


def build_service(request, service_name, success_redirect='service_list'):
    user = logic.is_patient(request.user)

    if user:
        # user_id = user.id
        service_id = Service.objects.get(name__iexact=service_name).id
        print(service_id)

        return redirect(success_redirect)

    return redirect(logic.get_redirect_url(user))


###############################################################################
def get_service_list(request):
    return build_service_list(request,
                              template='service/service_list.html',
                              context=forms.ContextServiceList)


###############################################################################
def get_food_list(request):
    return build_service_list(request,
                              template='service/food_list.html',
                              context=forms.ContextFoodList)


def get_eating(request):
    return build_service(request, "Принести еду")


def get_drinking(request):
    return build_service(request, "Принести попить")


###############################################################################
def get_baby_list(request):
    return build_service_list(request,
                              template='service/baby_list.html',
                              context=forms.ContextBabyList)


def bring_baby(request):
    return build_service(request, "Принести ребенка")


def carry_out_baby(request):
    return build_service(request, "Унести ребенка")


###############################################################################
def get_escort_list(request):
    return build_service_list(request,
                              template='service/escort_list.html',
                              context=forms.ContextEscortList)


def escort_to_wc(request):
    return build_service(request, "Сопроводить в туалет")


def escort_to_wash(request):
    return build_service(request, "Помочь помыться")


def escort_to_procedure(request):
    return build_service(request, "Сопроводить на процедуру")


###############################################################################
def alert(request):
    return build_service(request, "ALERT")


###############################################################################
def fun(request):
    return redirect('service_list')


###############################################################################
def get_archive(request):
    return redirect('service_list')
