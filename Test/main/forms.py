from pyexpat import model
from django import forms
from .models import Car

class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields ="__all__"