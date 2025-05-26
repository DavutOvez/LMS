from django import forms
from .models import *
from departments.models import *
from positions.models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group , Permission

class EmployeeForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.ModelChoiceField(required=False,queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-select select2'}))
    ID_num = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER,widget=forms.Select(attrs={'class':'form-select select2'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    department = forms.ModelChoiceField(required=False,queryset=Department.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-select select2'}))
    position = forms.ModelChoiceField(required=False,queryset=Position.objects.filter(deleted_at = None),widget=forms.Select(attrs={'class':'form-select select2'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    emp_type = forms.MultipleChoiceField(choices=EMP_TYPE,widget=forms.SelectMultiple(attrs={'class':'form-select select2'}))
    grad_uni = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    grad_major = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    grad_year = forms.DateField(required=False,widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))


    class Meta:
        model = Employee
        exclude = ['deleted_at' , 'username']

class UserForm(UserCreationForm):
    username = forms.CharField(label='Enter employee username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Enter employee password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    role = forms.ModelChoiceField(queryset=Group.objects.all() , widget=forms.Select(attrs={'class':'form-select select2'}))



class RolesForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all(),widget = forms.CheckboxSelectMultiple())
    class Meta:
        model = Group
        fields = '__all__'