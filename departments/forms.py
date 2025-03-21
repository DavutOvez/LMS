from django import forms
from employees.models import *
from .models import Department

class DepartmentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    head_of_dep = forms.ModelChoiceField(queryset=Employee.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-select select2'}))
    class Meta:
        model = Department
        exclude = ['deleted_at']