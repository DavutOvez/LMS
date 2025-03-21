from django import forms
from .models import*

class SeasonForm(forms.ModelForm):
    name = forms.CharField(label='Enter name:',widget=forms.TextInput(attrs={'class':'form-control'}))
    start_date = forms.DateField(label='Enter Start Date:',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    end_date = forms.DateField(label='Enter End Date:',widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    
    class Meta:
        model = Season
        exclude = ['deleted_at']