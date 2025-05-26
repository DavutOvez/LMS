from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.utils import timezone
from django.core.paginator import Paginator  ,EmptyPage
# Create your views here.

def seasons_table(request):
    # for i in range(1,30):
    #     Season.objects.create(name = f'Season{i}',
                              
            # start_date = '2025-02-04',
            # end_date = '2025-02-04',
            # status = False)
    # Season.objects.all().delete()
    all = Season.objects.filter(deleted_at = None)
    page_n =request.GET.get('page',1)
    p = Paginator(all , 2)
    try:
        page = p.get_page(page_n)
    except EmptyPage:
        page = p.get_page(1)
    return render(request,'seasons/table.html',context={'page':page})

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