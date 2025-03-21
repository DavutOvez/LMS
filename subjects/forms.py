from django import forms
from .models import*

class SubjectForm(forms.ModelForm):
    name = forms.CharField(label="Enter subject's name:",widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Subject
        exclude = ['deleted_at']



class LevelForm(forms.ModelForm):
    name = forms.CharField(label='Enter name' ,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-select select2'}))
    price = forms.DecimalField(label='Enter Price' ,widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Level
        exclude = ['deleted_at']