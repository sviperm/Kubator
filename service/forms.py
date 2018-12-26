from . import url_names_config as names


def gen_context_form(url_name, button_value):

    return {
        'name': url_name,
        'url': url_name,
        'value': button_value,
    }


def gen_context_view(context_list):
    return {
        'context_forms': context_list,
    }


ContextServiceList = gen_context_view(
    [
        gen_context_form(names.ORDER_LIST, 'Мои заявки'),
        gen_context_form(names.ALERT, 'ALERT'),
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
