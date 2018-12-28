from django.contrib.auth.models import User
from .models import Order, OrderStatus, PatientProfile, MedWorkerProfile
from .handler import OrderDistributor


def is_patient(user):
    if user.groups.filter(name='patient').exists():
        return user
    return None


def get_orders_info(patient_id, is_done, creation_date=True, opening_date=True, closing_date=True):

    def get_names(order_querys):
        fio_list = []
        for order in order_querys:
            if order.worker:
                last = order.worker.user.last_name.title()
                first = order.worker.user.first_name[0].upper()
                middle = order.worker.middle_name[0].upper()

                fio_list.append(
                    f'{last} {first}.{middle}.'
                )
            else:
                fio_list.append(order.status.name)

        return fio_list

    datetime_format = "%Y-%m-%d %H:%M"  # "%Y-%m-%d %H:%M:%S"

    profile = PatientProfile.objects.get(user_id=patient_id)
    statuses = OrderStatus.objects.all().filter(done=is_done)
    orders = Order.objects.filter(patient=profile, status__in=statuses)

    # TODO достать из бд имена врачей по заказам
    # TODO дата: чм_начало - чм_конец

    if len(orders) > 0:

        to_zip = [
            [o.service.name for o in orders],
            get_names(orders),
        ]

        if creation_date:
            to_zip.append([o.creation_date.strftime(datetime_format) for o in orders])
        if opening_date:
            to_zip.append([o.opening_date.strftime(datetime_format) if o.opening_date else '' for o in orders])
        if closing_date:
            to_zip.append([o.closing_date.strftime(datetime_format) if o.closing_date else '' for o in orders])

        return {'info': zip(*to_zip)}

    return {}


def is_in_process(worker_id):
    dsys = OrderDistributor()
    order = dsys.get_order(worker_id)
    if order:
        if order.status == dsys.status_in_process:
            return True
    return False


def is_done(worker_id):
    dsys = OrderDistributor()
    order = dsys.get_order(worker_id)

    if not order:
        return True
    if order.status == dsys.status_done:
        return True

    return False


def get_user_fio(user_id, profile):
    user = User.objects.get(id=user_id)
    last = user.last_name
    first = user.first_name
    if profile == 'med':
        middle = user.medworkerprofile.middle_name
    if profile == 'pat':
        middle = user.patientprofile.middle_name

    return f"{last} {first} {middle}"
