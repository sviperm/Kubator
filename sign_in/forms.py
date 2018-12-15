from django.forms import Form, CharField, TextInput


class SignInForm(Form):
    pin_code = CharField(widget=TextInput(attrs={'type': 'number'}))
