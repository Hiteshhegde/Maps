from django import forms
from .models import Distance

class DistanceModelForm(forms.ModelForm):
    class Meta:
        model = Distance
        fields = ('destination', )