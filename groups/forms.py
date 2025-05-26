from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from subjects.models import *
from branches.models import *
from seasons.models import *
from rooms.models import *
from employees.models import *
from students.models import *

class GroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.filter(deleted_at = None),required=False,widget=forms.Select(attrs={'class':'form-select select2'})) 
    level = forms.ModelChoiceField(queryset=Level.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-select select2'}))
    
    branch = forms.ModelChoiceField(queryset=Branch.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-select select2'}))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    language = forms.MultipleChoiceField(choices=Group.LANGUAGE_CHOICES,widget=forms.SelectMultiple(attrs={'class':'form-select select2'}))
    part_of_day = forms.ChoiceField(choices=Group.PART_OF_DAY,widget=forms.Select(attrs={'class':'form-select select2'}))
    week_days = forms.MultipleChoiceField(choices=Group.DAYS,widget=forms.SelectMultiple(attrs={'class':'form-select select2'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time','class':'form-control'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time','class':'form-control'}))
    room = forms.ModelChoiceField(queryset=Room.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-select select2'}))
    

    class Meta:
        model = Group
        exclude = ['students' ,'season','teacher', 'deleted_at']
    def __init__(self, *args , **kwargs):
        super().__init__(*args ,**kwargs )
        field_order = ['name','subject','level','branch','language','capacity','room','part_of_day','week_days','start_time','end_time']
        self.fields = {key: self.fields[key] for key in field_order if key in self.fields}







class GroupStudentForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(deleted_at = None),widget = forms.SelectMultiple(attrs={'class':'form-select  select2'}))

    class Meta:
        model = Group
        fields = ['students']

