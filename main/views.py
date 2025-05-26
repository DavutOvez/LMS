from django.shortcuts import render , redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , authenticate , logout
from .forms import *
from django.contrib.auth.decorators import permission_required

# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def login_page(request):
    form = LoginForm(request)
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            u_n = form.cleaned_data.get('username')
            u_p = form.cleaned_data.get('password')
            user = authenticate(username = u_n, password = u_p)

            if user:
                login(request,user)
                return redirect('/')

    return render(request,'login.html', context={'form':form})

def logout_page(request):
    logout(request)
    return render(request,'logout.html')

def custom_403(request , exception):
    return render(request , 'errors/403.html',status=403)