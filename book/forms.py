from django import forms


class ReportForm(forms.Form):
    description = forms.CharField(
        max_length=500,
        label='Opis',
        required=True,
    )
