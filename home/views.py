from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *


def index(request):
    return render(request, 'index.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken.")
            return redirect("/register_page/")  # Corrected the URL

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect("/login_page/")

    return render(request, "register_page.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Username does not exist.")
            return redirect("/login_page/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid password. Please try again.")
            return redirect("/login_page/")
        else:
            login(request, user)
            return redirect("/student_page/")

    return render(request, 'login_page.html')
def logout_page(request):
    logout(request)
@login_required(login_url="login_page")
def student_page(request):
    if request.method=="POST":
        student_name=request.POST.get("student_name")
        student_addresh=request.POST.get("student_addresh")
        student_roll_number=request.POST.get("student_roll_number")
        student_section=request.POST.get("student_section")
        student_marks_math=request.POST.get("student_marks_math")
        student_marks_Digital_logic=request.POST.get("student_marks_Digital_logic")
        student_marks_programing=request.POST.get("student_marks_programing")
        student_marks_discrete=request.POST.get("student_marks_discrete")
    
    return render(request,"student_page.html")

