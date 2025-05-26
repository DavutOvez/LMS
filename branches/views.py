from django.shortcuts import render , redirect
from .forms import*
from .models import*
from django.utils import timezone
from django.core.paginator import Paginator  ,EmptyPage
# Create your views here.

def branch_table(request):
    all = Branch.objects.filter(deleted_at = None)
    page_n = request.GET.get('page',1)
    p = Paginator(all , 10)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)
    return render(request,'branches/table.html',{'page':page})

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

