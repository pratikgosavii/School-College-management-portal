from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import *
from login.models import login_teacher, login_principle



# Create your views here.


def loginpage(request):
    return render(request, 'login.html')


def loginidentifier(request):

    if request.method == 'POST':
        username = request.POST['user_name_principle']
        password = request.POST['password_principle']
    identifier=None
    identifier=None
    identifier = login_principle.objects.filter(user_name_principle=username, password_principle=password).exists()
    identifier2 =login_teacher.objects.filter(user_name_teacher=username, password_teacher=password).exists()
    
    
    if identifier is True:
        return render(request, 'principlehome.html')
        
    if identifier2 is True:
        return render(request, 'teacherhome.html')

    else :
        return render(request, 'login.html')

        
 






       


    