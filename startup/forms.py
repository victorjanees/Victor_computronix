from django import forms
from .models import Raise_request

class Raise_Request_Form(forms.Form):
    customer_name = forms.CharField(max_length = 20)
    customer_mobile_number = forms.CharField(max_length=10)
    service_you_need = forms.CharField(max_length = 20)
    details_of_it = forms.CharField(widget = forms.Textarea, required=False)

class Raise_Request_Model_Form(forms.ModelForm):
    class Meta:
        model = Raise_request
        fields = ['customer_name', 'customer_mobile_number', 'service_you_need', 'details_of_it']