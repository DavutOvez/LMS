from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator  ,EmptyPage
from django.utils import timezone
# Create your views here.

def departments_table(request):
    all = Department.objects.filter(deleted_at = None)
    page_n = request.GET.get('page',1)
    p = Paginator(all , 10)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)
    return render(request,'departments/table.html',context={'page':page})

def department_delete(request , pk):
    department = Department.objects.get(pk = pk)
    department.deleted_at = timezone.now()
    department.save()
    return redirect('/departments/table/')

def department_edit(request,pk):
    department = Department.objects.get(pk = pk)
    form = DepartmentForm(instance=department)
    if request.method == 'POST':
        form = DepartmentForm( request.POST ,instance=department)
        if form.is_valid():
            form.save()
            return redirect('/departments/table/')
    return render(request,'departments/edit.html',context={'form':form})

def department_create(request):
    form = DepartmentForm()
    if request.method == 'POST':
        form = DepartmentForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect('/departments/table/')
    return render(request,'departments/create.html',context={'form':form})