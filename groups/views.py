from django.shortcuts import render , redirect
from .forms import *
from .models import*
# Create your views here.

def groups_table(request):
    all = Group.objects.all()
    return render(request,'groups/table.html',context={'all':all})

def group_delete(request , pk):
    group = Group.objects.get(pk = pk)
    group.delete()
    return redirect('/groups/table/')

def group_edit(request,pk):
    group = Group.objects.get(pk = pk)
    form = GroupForm(instance=group)
    if request.method == 'POST':
        form = GroupForm( request.POST ,instance=group)
        if form.is_valid():
            form.save()
            return redirect('/groups/table/')
    return render(request,'groups/edit.html',context={'form':form})

def group_create(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect('/groups/table/')
    return render(request,'groups/create.html',context={'form':form})

def group_stu_create(request):
    form = GroupStudentForm()
    # if request.method = 'POST'
    return render(request,'groups/stu-create.html',context={'form':form})