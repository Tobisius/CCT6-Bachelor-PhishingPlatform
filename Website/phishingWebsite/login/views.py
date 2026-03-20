from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from sqlmanager.views import *

tableName = "UserData"

def index(request):
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"Email: {email}, Password: {password}")
        
        hashedPasswordDatabase = getHashedPassword(tableName, email)
        print("Password from db: ", hashedPasswordDatabase)
        if hashedPasswordDatabase == password:
            return redirect("login:loginSuccess")
        else: 
            return HttpResponse("Login failed....")
        
    return render(request, 'login/loginPage.html')

def loginSuccess(request):
    return HttpResponse("Login Success")

