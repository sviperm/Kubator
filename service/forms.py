from django import forms


class OrderReportForm(forms.Form):
    report = forms.CharField(widget=forms.Textarea, label='')
