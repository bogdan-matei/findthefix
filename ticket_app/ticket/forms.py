from django import forms
from .models import Model


class TicketForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", max_length=30, empty_value=True, required=True)
    last_name = forms.CharField(label="Last Name", max_length=30, empty_value=True, required=True)
    unique_id = forms.CharField(label="ID Number", max_length=30, empty_value=True, required=True)
    street_address = forms.CharField(label="Street Address", max_length=100, empty_value=True, required=True)
    email_address = forms.CharField(label="Email Address", max_length=40, empty_value=True, required=True)
    credit_card = forms.CharField(label="Credit Card", max_length=16, widget=forms.TextInput(attrs={'type': 'number'}),
                                  required=True)

    class Meta:
        model = Model
        exclude = ('purchase_date',)
