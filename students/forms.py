from django import forms
from .models import*

class StudentForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    fullname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # student_ID = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER , widget=forms.Select(attrs={'class':'form-control select2'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    school_type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    school_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    school_class = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
                                                               


    class Meta:
        model = Student
        exclude = ['deleted_at' , 'student_ID']