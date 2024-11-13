from django.shortcuts import render, redirect,get_object_or_404
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
@login_required(login_url="/login_page")
def student_page(request):
    
    if request.method=="POST":
        data=request.POST
        student_name=data.get("student_name")
        student_address=data.get("student_address")
        student_roll_number=data.get("student_roll_number")
        student_section=data.get("student_section")
        student_marks_math=data.get("student_marks_math")
        student_marks_Digital_logic=data.get("student_marks_Digital_logic")
        student_marks_programming=data.get("student_marks_programming")
        student_marks_discrete=data.get("student_marks_discrete")
        student.objects.create(
        student_name=student_name,
        student_address=student_address,
        student_roll_number=student_roll_number,
        student_section=student_section,
        student_marks_math=student_marks_math,
        student_marks_Digital_logic=student_marks_Digital_logic,
        student_marks_programming=student_marks_programming,
        student_marks_discrete=student_marks_discrete,
        )
        
    queryset=student.objects.all()
    context={"students":queryset}
    return render(request,"student_page.html",context)

@login_required(login_url="/login_page")
def update(request,id):
    queryset=get_object_or_404(student,id=id)
    if request.method=="POST":
        data=request.POST
        student_name=data.get("student_name")
        student_address=data.get("student_address")
        student_roll_number=data.get("student_roll_number")
        student_section=data.get("student_section")
        student_marks_math=data.get("student_marks_math")
        student_marks_Digital_logic=data.get("student_marks_Digital_logic")
        student_marks_programming=data.get("student_marks_programming")
        student_marks_discrete=data.get("student_marks_discrete")
    
        queryset.student_name=student_name
        queryset.student_address=student_address
        queryset.student_roll_number=student_roll_number
        queryset.student_section=student_section
        queryset.student_marks_math=student_marks_math
        queryset.student_marks_Digital_logic=student_marks_Digital_logic
        queryset.student_marks_programming=student_marks_programming
        queryset.student_marks_discrete=student_marks_discrete
        queryset.save()
        queryset=student.objects.all()
        
        return redirect ("/student_page/")
    context={"students":queryset}
    return render(request,"update.html",context)

def result(request,id):
    queryset=get_object_or_404(student,id=id)
    student_marks_Digital_logic=int(queryset.student_marks_Digital_logic) if queryset.student_marks_Digital_logic else 0
    total=(int(queryset.student_marks_math)+student_marks_Digital_logic+
           int(queryset.student_marks_discrete)+int(queryset.student_marks_programming))
    max_numb=400
    percentage=(total/max_numb)*100
    if percentage >= 90:
        Grade = "A"
    elif percentage >= 80:
        Grade = "B"
    elif percentage >= 70:
        Grade = "C"
    elif percentage >= 60:
        Grade = "D"
    else:
        Grade = "F"
    if percentage<40:
        result="fail"
    else:
        result="pass"
    queryset=student.objects.get(id=id)
    context={"student":queryset,"total":total,"max_numb":max_numb,
             "percentage":percentage,"result":result,"Grade":Grade}
    
    return render(request,"result.html",context)

def delete(request,id):
    queryset=student.objects.get(id=id)
    queryset.delete()
    return redirect("/student_page/")
def logout_page(request):
    logout(request)
    return redirect("/index/")

