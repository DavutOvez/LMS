from django.shortcuts import render , redirect
from .forms import *
from .models import*
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator  ,EmptyPage
# Create your views here.

def groups_table(request):
    all = Group.objects.all()
    search_form = SearchForm(request.GET or None)
    subject = request.GET.get('subject',None)
    if subject:
        all = all.filter(level__subject_id = subject )
    level = request.GET.get('level',None)
    if level:
        all = all.filter(level_id = level )

    name = request.GET.get('name',None)
    if name:
        all = all.filter(name__contains = name )

    part_of_day = request.GET.get('part_of_day',None)
    if part_of_day:
        all = all.filter(part_of_day = part_of_day )
    page_n = request.GET.get('page',1)
    p = Paginator(all , 10)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)

    teachers = Employee.objects.all()
    return render(request,'groups/table.html',context={'page':page , 'search_form':search_form,
                                                       'teachers':teachers})

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



def add_teacher(request):
    group_id = request.POST.get('group_id',None)
    emp_id = request.POST.get('emp_id',None)

    if group_id:
        group = Group.objects.get(id=group_id)
        if emp_id:
            emp = Employee.objects.get(id=emp_id)

            group.teacher = emp
            group.save()
        else:
            group.teacher = None
            group.save()

    return redirect('/groups/table/')

def student(request , pk):
    group = Group.objects.get(id = pk)
    group_students = group.students.all()
    students = Student.objects.all().exclude(groups = group)

    if request.method == 'POST':
        student_id = request.POST.get('student_id' , None)
        if student_id:
            student = Student.objects.get(id = student_id)
            group.students.add(student)
        
    return render(request,'groups/student_list.html',context={'students':group_students,
                                                              'group':group,
                                                              'all_students':students})


def remove_student(request,sp,gp):
    student = Student.objects.get(id=sp)
    group = Group.objects.get(id = gp)
    group.students.remove(student)
    return redirect(f'/groups/add_student/{group.id}/')