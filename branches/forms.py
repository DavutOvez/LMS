from django import forms
from .models import Branch
from employees.models import Employee

class BranchForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    head_of_branch = forms.ModelChoiceField(queryset=Employee.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-control select2'}))

    class Meta:
        model = Branch
        exclude = ['deleted_at']
