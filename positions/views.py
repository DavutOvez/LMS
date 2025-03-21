from django.shortcuts import render , redirect
from .forms import PositionForm
from .models import Position
from django.utils import timezone
# Create your views here.

def position_table(request):
    positions = Position.objects.filter(deleted_at = None)
    return render(request,'positions/table.html',{'all':positions})

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