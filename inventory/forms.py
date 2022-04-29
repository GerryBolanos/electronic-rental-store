from django import forms
from django.forms import ModelForm
from .models import Electronics, Rents, Customer


ELECTRONIC_TYPES = [('laptop', 'Laptop'), ('tablet', 'Tablet'), ('mobilephone', 'Phone')]


class DateInput(forms.DateInput):
    input_type = 'date'


class AddNewElectronicForm(ModelForm):
    electype = forms.CharField(label="Type", widget=forms.Select(choices=ELECTRONIC_TYPES))

    class Meta:
        model = Electronics
        fields = ['elecid', 'model', 'stock', 'os', 'screen_size', 'storage', 'gpu', 'refresh_rate', 'carrier']
        # fields = '__all__'


class RemoveItemForm(forms.Form):

    elecid = forms.IntegerField(label="ElecId")


class RentItemForm(ModelForm):
    custid = forms.IntegerField()
    elecid = forms.IntegerField()

    class Meta:
        model = Rents
        fields = ['rental_date', 'return_date']
        widgets = {
            'rental_date': DateInput(),
            'return_date': DateInput(),
        }
    # class Meta:
    #     model = Rents
