from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.utils import timezone
# Create your views here.

def seasons_table(request):
    all = Season.objects.filter(deleted_at = None)
    return render(request,'seasons/table.html',context={'all':all})

def season_delete(request , pk):
    season = Season.objects.get(pk = pk)
    season.deleted_at = timezone.now()
    season.save()
    return redirect('/seasons/table/')

def season_edit(request,pk):
    season = Season.objects.get(pk = pk)
    form = SeasonForm(instance=season)
    if request.method == 'POST':
        form = SeasonForm( request.POST ,instance=season)
        if form.is_valid():
            form.save()
            return redirect('/seasons/table/')
    return render(request,'seasons/edit.html',context={'form':form})

def season_create(request):
    form = SeasonForm()
    if request.method == 'POST':
        form = SeasonForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect('/seasons/table/')
    return render(request,'seasons/create.html',context={'form':form})