from django.shortcuts import render , redirect
from .forms import PositionForm
from .models import Position
from django.utils import timezone
from django.core.paginator import Paginator  ,EmptyPage
# Create your views here.

def position_table(request):
    all = Position.objects.filter(deleted_at = None)
    page_n = request.GET.get('page',1)
    p = Paginator(all , 10)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)
    return render(request,'positions/table.html',{'page':page})

def position_create(request):
    form = PositionForm()
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_table')
    return render(request,'positions/create.html',{'form':form})

def position_edit(request,pk):
    position = Position.objects.get(id=pk)
    form = PositionForm(instance=position)
    if request.method == 'POST':
        form = PositionForm(request.POST,instance=position)
        if form.is_valid():
            form.save()
            return redirect('position_table')
    return render(request,'positions/edit.html',{'form':form})

def position_delete(request,pk):
    position = Position.objects.get(id=pk)
    position.deleted_at = timezone.now()
    position.save()
    return redirect('position_table')