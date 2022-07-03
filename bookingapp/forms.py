from pyexpat import model
from django import forms

from .models import Booking , doctor ,clinic,clininfo ,num_of_building

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        

class DoctorForm(forms.ModelForm):
    class Meta:
        model = doctor
        fields = '__all__'


class clinicForm(forms.ModelForm):
    class Meta:
        model = clinic
        fields = '__all__'


class cliccForm(forms.ModelForm):
    class Meta:
        model = clininfo
        fields = '__all__'

class buildingForm(forms.ModelForm):
    class Meta:
        model = num_of_building
        fields= '__all__'