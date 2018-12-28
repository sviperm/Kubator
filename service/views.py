from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from manager import helpers as manager
from .handler import OrderDistributor
from .models import Service
from .forms import OrderReportForm
from . import contexts
from . import helpers
from . import url_names_config as names


@user_passes_test(manager.is_patient, redirect_field_name='', login_url='account:home')
def build_service_list(request, template, context):
    return render(request, template, context)


@user_passes_test(manager.is_patient, redirect_field_name='', login_url='account:home')
def build_service(request, service_name, success_redirect=names.SERVICE_LIST):
    service_id = Service.objects.get(name__iexact=service_name).id

    dsys = OrderDistributor()  # init order distribution system
    dsys.add_order(request.user.id, service_id)

    return redirect(success_redirect)


###############################################################################
def get_service_list(request):
    context = contexts.ContextServiceList
    context.update({"my_orders": contexts.ContextMyOrders})
    return build_service_list(request,
                              template='service/service_list.html',
                              context=contexts.ContextServiceList)


###############################################################################
def get_food_list(request):
    return build_service_list(request,
                              template='service/food_list.html',
                              context=contexts.ContextFoodList)


def get_eating(request):
    return build_service(request, "Принести еду")


def get_drinking(request):
    return build_service(request, "Принести попить")


###############################################################################
def get_baby_list(request):
    return build_service_list(request,
                              template='service/baby_list.html',
                              context=contexts.ContextBabyList)


def bring_baby(request):
    return build_service(request, "Принести ребенка")


def carry_out_baby(request):
    return build_service(request, "Унести ребенка")


###############################################################################
def get_escort_list(request):
    return build_service_list(request,
                              template='service/escort_list.html',
                              context=contexts.ContextEscortList)


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
    context = helpers.get_orders_info(
        request.user.id, is_done=False, closing_date=False)
    context.update(contexts.ContextArchive)

    return render(request, 'service/order_list.html', context=context)


def get_archive(request):
    context = helpers.get_orders_info(
        request.user.id, is_done=True, creation_date=False)
    return render(request, 'service/archive.html', context=context)


###############################################################################
@user_passes_test(manager.is_medworker, redirect_field_name='', login_url='account:home')
def get_new_order(request):
    worker_id = request.user.id
    dsys = OrderDistributor()
    context = {}

    if helpers.is_in_process(worker_id):
        return redirect(names.CLOSE_ORDER)

    context.update({'info': dsys.get_order_info(worker_id)})
    context.update(contexts.ContextOpenOrder)

    return render(request, 'service/medworker.html', context)


@user_passes_test(manager.is_medworker, redirect_field_name='', login_url='account:home')
def open_order(request):
    worker_id = request.user.id
    if not helpers.is_in_process(worker_id):
        dsys = OrderDistributor()
        dsys.open(worker_id)
    return redirect(names.CLOSE_ORDER)


@user_passes_test(manager.is_medworker, redirect_field_name='', login_url='account:home')
def close_order(request):
    if request.method == "POST":
        form = OrderReportForm(request.POST)
        if form.is_valid():
            report = form.cleaned_data['report']

            dsys = OrderDistributor()
            dsys.close(request.user.id, report)
            return redirect(names.MEDWORKER_HOME)

    form = OrderReportForm()
    dsys = OrderDistributor()
    context = contexts.ContextCloseOrder
    context.update({'info': dsys.get_order_info(request.user.id)})
    context.update({'form': form})

    return render(request, 'service/close_order.html', context)
