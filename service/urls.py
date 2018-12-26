from django.urls import path
from . import views
from . import url_names_config as names

urlpatterns = [
    path('', views.get_service_list, name=names.SERVICE_LIST),
    path('alert/', views.alert, name=names.ALERT),
    path('fun/', views.fun, name=names.FUN),
    path('my_orders/', views.get_order_list, name=names.ORDER_LIST),
    path('archive/', views.get_archive, name=names.ARCHIVE),

    path('escort/', views.get_escort_list, name=names.ESCORT_LIST),
    path('wc/', views.escort_to_wc, name=names.ESCORT_WC),
    path('wash/', views.escort_to_wash, name=names.ESCORT_WASH),
    path('procedure/', views.escort_to_procedure, name=names.ESCORT_PROCEDURE),

    path('baby/', views.get_baby_list, name=names.BABY_LIST),
    path('bring/', views.bring_baby, name=names.BRING_BABY),
    path('carry_out/', views.carry_out_baby, name=names.CARRY_OUT_BABY),

    path('food/', views.get_food_list, name=names.FOOD_LIST),
    path('eating/', views.get_eating, name=names.FOOD_EATING),
    path('drinking/', views.get_drinking, name=names.FOOD_DRINKING),

    path('medworker/', views.medworker, name='medworker'),

]
