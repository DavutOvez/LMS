from django.shortcuts import render , redirect
from .forms import *
from .models import Employee
from django.utils import timezone
# Create your views here.



def employee_table(request):
    employees = Employee.objects.filter(deleted_at = None)
    return render(request,'employees/table.html',{'all':employees})

def employee_create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_table')
    return render(request,'employees/create.html',{'form':form})

def employee_edit(request,pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_table')
    return render(request,'employees/edit.html',{'form':form})

def employee_delete(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.deleted_at = timezone.now()
    employee.save()
    return redirect('employee_table')

def detail(request , pk):
    
    employee = Employee.objects.get(id=pk)
    return render(request , 'employees/profile.html' , context={'employee':employee})

def create_user(request,pk):
    employee = Employee.objects.get(id=pk)
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.save()
            employee.username = username
            employee.save()
            return redirect('/employees/table/')
    return render(request,'employees/user_create.html',context={'form':form,'employee':employee})