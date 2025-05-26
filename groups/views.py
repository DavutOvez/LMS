from django.shortcuts import render , redirect
from .forms import *
from .models import*
from django.core.paginator import Paginator  ,EmptyPage
# Create your views here.

def groups_table(request):
    all = Group.objects.all()
    page_n = request.GET.get('page',1)
    p = Paginator(all , 10)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)
    return render(request,'groups/table.html',context={'page':page})

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
            group = form.save(commit=False)
            active_season = Season.objects.get(status = True)
            group.season = active_season
            group.save()
            return redirect('/groups/table/')
    return render(request,'groups/create.html',context={'form':form})

def group_timetable(request):
    rooms= Room.objects.all()
    days = [ 1 , 2 , 3 , 3 , 5 , 6 ]
    timetable = []

    morning_groups = Group.objects.filter(part_of_day = 'Morning')
    for room in rooms:
        groups = morning_groups.filter(room = room)
        group1 = groups.filter(week_days__contains = '1').first()
        group2 = groups.filter(week_days__contains = '2').first()
        group3 = groups.filter(week_days__contains = '3').first()
        group4 = groups.filter(week_days__contains = '4').first()
        group5 = groups.filter(week_days__contains = '5').first()
        group6 = groups.filter(week_days__contains = '6').first()
        timetable.append( [room.name , group1 ,group2 ,group3 , group4 , group5 , group6 ,])
    return render(request , 'groups/timetable.html' , context={'timetable':timetable})