from patient.models import PatientProfile
from med_worker.models import MedWorkerProfile


def gen_username(profile):
    if profile == 'patient':
        object_num = PatientProfile.objects.count() + 1
    elif profile == 'medworker':
        object_num = MedWorkerProfile.objects.count() + 1
    else:
        return ValueError
    return f'{profile}_{object_num}'


def is_manager(user):
    return user.groups.filter(name='manager').exists()


def is_patient(user):
    return user.groups.filter(name='patient').exists()


def is_medworker(user):
    return user.groups.filter(name='medworker').exists()
