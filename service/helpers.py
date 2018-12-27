from .models import Order, OrderStatus, PatientProfile
from .handler import OrderDistributor


def is_patient(user):
    if user.groups.filter(name='patient').exists():
        return user
    return None


def get_orders_info(patient_id, is_done, creation_date=True, opening_date=True, closing_date=True):
    datetime_format = "%Y-%m-%d %H:%M:%S"

    profile = PatientProfile.objects.get(user_id=patient_id)
    statuses = OrderStatus.objects.all().filter(done=is_done)
    orders = Order.objects.filter(patient=profile, status__in=statuses)

    if len(orders) > 0:

        to_zip = [
            [o.service.name for o in orders],
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
