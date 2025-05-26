from django.shortcuts import render , redirect
from .models import Student
from .forms import StudentForm
from django.utils import timezone
from django.core.paginator import Paginator  ,EmptyPage


# Create your views here.


def generate_student_ID():
    year = f'{timezone.now().year}'
    s_count = Student.objects.filter(created_at__year= timezone.now().year).count()

    return year + str(s_count + 1).zfill(4)

def student_table(request):
    all = Student.objects.filter(deleted_at = None)
    page_n = request.GET.get('page',1)
    p = Paginator(all , 10)
    try:
        page = p.page(page_n)
    except EmptyPage:
        page = p.page(1)
    return render(request,'students/table.html',{'page':page})

def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
    
            student =form.save(commit=False)
            student.student_ID = generate_student_ID()
            student.save()
            return redirect('/students/table/')
    return render(request,'students/create.html',{'form':form})

def student_edit(request,pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students/table/')
    return render(request,'students/edit.html',{'form':form})

def student_delete(request,pk):
    student = Student.objects.get(id=pk)
    student.deleted_at = timezone.now()
    student.save()
    return redirect('/students/table/')

def detail(request , pk):
    
    student = Student.objects.get(id=pk)
    return render(request , 'students/profile.html' , context={'student':student})