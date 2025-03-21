from django.shortcuts import render
from django.http import JsonResponse



# Create your views here.
from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.utils import timezone
# Create your views here.

def subjects_table(request):
    all = Subject.objects.filter(deleted_at = None)
    return render(request,'subjects/table.html',context={'all':all})

def subject_delete(request , pk):
    subject = Subject.objects.get(pk = pk)
    subject.deleted_at = timezone.now()
    subject.save()

    return redirect('/subjects/table/')

def subject_edit(request,pk):
    subject = Subject.objects.get(pk = pk)
    form = SubjectForm(instance=subject)
    if request.method == 'POST':
        form = SubjectForm( request.POST ,instance=subject)
        if form.is_valid():
            form.save()
            return redirect('/subjects/table/')
    return render(request,'subjects/edit.html',context={'form':form})

def subject_create(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect('/subjects/table/')
    return render(request,'subjects/create.html',context={'form':form})

#-----------------------------------------------------

def levels_table(request):
    all = Level.objects.filter(deleted_at = None)
    return render(request,'levels/table.html',context={'all':all})

def level_delete(request , pk):
    level = Level.objects.get(pk = pk)
    level.deleted_at = timezone.now()
    level.save()
    return redirect('/levels/table/')

def level_edit(request,pk):
    level = Level.objects.get(pk = pk)
    form = LevelForm(instance=level)
    if request.method == 'POST':
        form = LevelForm( request.POST ,instance=level)
        if form.is_valid():
            form.save()
            return redirect('/levels/table/')
    return render(request,'levels/edit.html',context={'form':form})

def level_create(request):
    form = LevelForm()
    if request.method == 'POST':
        form = LevelForm( request.POST )
        if form.is_valid():
            form.save()
            return redirect('/levels/table/')
    return render(request,'levels/create.html',context={'form':form})


def get_levels(request):
    subject_id = request.GET.get('subject_id')
    if subject_id:
        levels = Level.objects.filter(subject_id = subject_id).values('id','name')
        return JsonResponse(list(levels) , safe = False)
    return JsonResponse([] , safe= False)