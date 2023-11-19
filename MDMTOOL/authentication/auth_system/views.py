import os
import zipfile
import pandas as pd
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ImportForm
from .models import ImportFile, ImportRecord


# Create your views here.

@login_required
def HomePage(request):
    return render(request, 'auth_system/index.html', {})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request, 'auth_system/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-Page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'auth_system/login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('login-page')

def test(request):
    return render(request, 'auth_system/test.html', {})


def nibin456_view(request):
    return render(request, 'auth_system/NIBIN456.html')


def import_view(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            import_file = form.save()
            
            # parse uploaded file and save records
            # ...
            
            return redirect('auth_system_complete')
    else:
        form = ImportForm()
    
    return render(request, 'auth_system/main.html', {'form': form})

def import_complete(request):
    return render(request, 'auth_system/complete.html')

