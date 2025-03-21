from django.shortcuts import render , redirect
from .forms import*
from .models import*
from django.utils import timezone
# Create your views here.

def branch_table(request):
    branches = Branch.objects.filter(deleted_at = None)
    return render(request,'branches/table.html',{'all':branches})

def branch_create(request):
    form = BranchForm()
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch_table')
    return render(request,'branches/create.html',{'form':form})

def branch_edit(request,pk):
    branch = Branch.objects.get(id=pk)
    form = BranchForm(instance=branch)
    if request.method == 'POST':
        form = BranchForm(request.POST,instance=branch)
        if form.is_valid():
            form.save()
            return redirect('branch_table')
    return render(request,'branches/edit.html',{'form':form})

def branch_delete(request,pk):
    branch = Branch.objects.get(id=pk)
    branch.deleted_at = timezone.now()
    branch.save()
    return redirect('branch_table')

