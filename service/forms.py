from django import forms


class OrderReportForm(forms.ModelForm):
    report = forms.CharField(widget=forms.Textarea)
