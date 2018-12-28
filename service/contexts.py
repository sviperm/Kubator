from . import url_names_config as names


def gen_context_form(url_name, button_value, button_class="btn btn-default"):

    return {
        'url': url_name,
        'value': button_value,
        'class': button_class,
    }


def gen_context_view(context_list):
    return {
        'context_forms': context_list,
    }


ContextMyOrders = gen_context_form(names.ORDER_LIST, 'Мои заявки')
ContextExit = {}

ContextServiceList = gen_context_view(
    [
        gen_context_form(names.ALERT, 'ALERT', button_class="btn btn-danger"),
        gen_context_form(names.BABY_LIST, 'Ребенок'),
        gen_context_form(names.ESCORT_LIST, 'Сопровождение'),
        gen_context_form(names.FOOD_LIST, 'Питание'),
        gen_context_form(names.FUN, 'Развлечения'),
    ]
)

ContextFoodList = gen_context_view(
    [
        gen_context_form(names.FOOD_EATING, 'Принести еды'),
        gen_context_form(names.FOOD_DRINKING, 'Принести попить'),
    ]
)

ContextBabyList = gen_context_view(
    [
        gen_context_form(names.BRING_BABY, 'Принести ребенка'),
        gen_context_form(names.CARRY_OUT_BABY, 'Унести ребенка'),
    ]
)

ContextEscortList = gen_context_view(
    [
        gen_context_form(names.ESCORT_WC, 'Отвести в туалет'),
        gen_context_form(names.ESCORT_WASH, 'Помочь помыться'),
        gen_context_form(names.ESCORT_PROCEDURE, 'Отвести на процедуру'),
    ]
)

ContextArchive = gen_context_view([
    gen_context_form(names.ARCHIVE, 'Архив заявок'),
])

ContextOpenOrder = gen_context_view([
    gen_context_form(names.OPEN_ORDER, 'Открыть заявку'),
])

ContextCloseOrder = gen_context_view([
    gen_context_form(names.CLOSE_ORDER, 'Закрыть заявку'),
])
