from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from .handler import OrderDistributor
from manager import helpers
from .models import Service, Order, OrderStatus, PatientProfile
from . import forms
from . import logic


@login_required(redirect_field_name='')
@user_passes_test(helpers.is_patient, redirect_field_name='')
def build_service_list(request, template, context):
    user = logic.is_patient(request.user)
    if user:
        return render(request, template, context)
    return redirect(logic.get_redirect_url(user))


@login_required(redirect_field_name='')
@user_passes_test(helpers.is_patient, redirect_field_name='')
def build_service(request, service_name, success_redirect='service_list'):
    user = logic.is_patient(request.user)

    if user:
        user_id = user.id
        service_id = Service.objects.get(name__iexact=service_name).id

        dsys = OrderDistributor()  # init order distribution system
        dsys.add_order(user_id, service_id)

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
def get_order_list(request):
    context = logic.get_orders_info(
        request.user.id, is_done=False, closing_date=False)
    context.update(forms.ContextArchive)

    return render(request, 'service/order_list.html', context=context)


def get_archive(request):
    context = logic.get_orders_info(
        request.user.id, is_done=True, creation_date=False)
    return render(request, 'service/archive.html', context=context)


@login_required(redirect_field_name='')
@user_passes_test(helpers.is_medworker, redirect_field_name='')
def medworker(request):
    return render(request, 'service/medworker.html')
