from django.shortcuts import render , redirect
from .forms import *
from .models import Employee
from django.utils import timezone
from django.core.paginator import Paginator  ,EmptyPage
from django.contrib.auth.models import Group

# Create your views here.



def employee_table(request):
    all = Employee.objects.filter(deleted_at = None)
    page_n = request.GET.get('page',1)
    p = Paginator(all , 10)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)
    return render(request,'employees/table.html',{'page':page})

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
            role = form.cleaned_data.get('role')
            user = form.save()
            user.groups.add(role)
            username = form.save()
            employee.username = username
            employee.save()
            return redirect('/employees/table/')
    return render(request,'employees/user_create.html',context={'form':form,'employee':employee})


def roles_table(request):
    all_roles = Group.objects.all()
    return render(request , 'roles/table.html',context={'all':all_roles})


def role_create(request):
    form = RolesForm()
    if request.method == 'POST':
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/roles/table/')
    return render(request,'roles/create.html',{'form':form})


def role_edit(request,pk):
    role = Group.objects.get(id=pk)
    form = RolesForm(instance=role)
    if request.method == 'POST':
        form = RolesForm(request.POST,instance=role)
        if form.is_valid():
            form.save()
            return redirect('/roles/table/')
    return render(request,'roles/edit.html',{'form':form})