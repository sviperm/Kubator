def is_patient(user):
    if user.groups.filter(name='patient').exists():
        return user
    return None


def get_redirect_url(user):
    return 'service_list'
