from django.urls import path
from . import views
from . import url_names_config as names

urlpatterns = [
    path('patient/', views.get_service_list, name=names.SERVICE_LIST),
    path('patient/alert/', views.alert, name=names.ALERT),
    path('patient/fun/', views.fun, name=names.FUN),
    path('patient/my_orders/', views.get_order_list, name=names.ORDER_LIST),
    path('patient/archive/', views.get_archive, name=names.ARCHIVE),

    path('patient/escort/', views.get_escort_list, name=names.ESCORT_LIST),
    path('patient/wc/', views.escort_to_wc, name=names.ESCORT_WC),
    path('patient/wash/', views.escort_to_wash, name=names.ESCORT_WASH),
    path('patient/procedure/', views.escort_to_procedure,
         name=names.ESCORT_PROCEDURE),

    path('patient/baby/', views.get_baby_list, name=names.BABY_LIST),
    path('patient/bring/', views.bring_baby, name=names.BRING_BABY),
    path('patient/carry_out/', views.carry_out_baby, name=names.CARRY_OUT_BABY),

    path('patient/food/', views.get_food_list, name=names.FOOD_LIST),
    path('patient/eating/', views.get_eating, name=names.FOOD_EATING),
    path('patient/drinking/', views.get_drinking, name=names.FOOD_DRINKING),

    path('medworker/', views.get_new_order, name=names.MEDWORKER_HOME),
    path('medworker/open', views.open_order, name=names.OPEN_ORDER),
    path('medworker/close', views.close_order, name=names.CLOSE_ORDER),

]
