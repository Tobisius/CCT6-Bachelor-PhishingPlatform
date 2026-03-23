from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from sqlmanager.views import *

tableName = "UserData"

def index(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        passwordFromFrontEnd = request.POST.get("password")
        
        hashedPasswordDatabase = getHashedPassword(tableName, email)
        if hashedPasswordDatabase == passwordFromFrontEnd:
            
            request.session['user_email'] = email
            
            return redirect("login:loginSuccess")
        else: 
            return render(request, 'login/loginPage.html', {'error': 'Invalid credentials'})
        
    return render(request, 'login/loginPage.html')

def loginSuccess(request):
    return HttpResponse("Login Success")

