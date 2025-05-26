from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter your username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter your password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
