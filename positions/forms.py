from django import forms
from .models import Position
from departments.models import Department
from django.forms import ModelChoiceField

class PositionForm(forms.ModelForm):
    department = ModelChoiceField(queryset=Department.objects.filter(deleted_at = None) , widget=forms.Select(attrs={'class':'form-control select2'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Position
        exclude = ['deleted_at']