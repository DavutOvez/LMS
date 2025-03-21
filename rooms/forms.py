from django import forms
from .models import *

class RoomForm(forms.ModelForm):
    name = forms.CharField(label='Enter Name:',widget=forms.TextInput(attrs={'class':'form-control'}))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Room
        exclude = ['deleted_at']