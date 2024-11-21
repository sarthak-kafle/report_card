from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *
from matplotlib import pyplot as plt
from io import BytesIO
import base64
import pandas as pd
from django.http import JsonResponse
from django.conf import settings


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

def piechart(request):
    queryset = student.objects.all()
    student_data =[]
    count=0
    count1=0
    count2=0
    count3=0
    count4=0

    for student_obj in queryset:
        student_marks_Digital_logic = int(student_obj.student_marks_Digital_logic) if student_obj.student_marks_Digital_logic else 0
        total = (
            int(student_obj.student_marks_math) +
            student_marks_Digital_logic +
            int(student_obj.student_marks_discrete) +
            int(student_obj.student_marks_programming)
        )
        max_numb = 400
        percentage = (total / max_numb) * 100

        if percentage >= 90:
            Grade = "A"
            count=count+1
        elif percentage >= 80:
            Grade = "B"
            count1=count1+1
        elif percentage >= 70:
            Grade = "C"
            count2=count2+1
        elif percentage >= 60:
            Grade = "D"
            count3=count3+1
        else:
            Grade = "F"
            count4=count4+1

        result = "pass" if percentage >= 40 else "fail"

        # Append the student's data to the list
        student_data.append({
            "student": student_obj,
            "total": total,
            "percentage": percentage,
            "Grade": Grade,
            "result": result,
        })
    
    data_labels = [">90%", ">80%", ">70%", ">60%", "Fail"]
    sales = [count, count1, count2, count3, count4]
    my_explode = [0.2, 0, 0, 0, 0]
    my_colors = ["green", "blue", "yellow", "red", "orange"]

    # Create the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sales, labels=data_labels, explode=my_explode, shadow=True, colors=my_colors, autopct='%1.1f%%')
    plt.title("Percentage Scores of Students")

    # Save the chart to a string buffer
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close()

    # Pass data to the template
    context = {
        "student_data": student_data,
        "students": queryset,
        "count": count,
        "chart_data": chart_data,
    }
    return render(request, "piechart.html", context)

def new_func():
    student_data = []
    return student_data


def data_export(request):
    objs=student.objects.all()
    data=[]
    for obj in objs:
       data.append( {
           "student_name":obj.student_name,
           "student_address":obj.student_address,
           "student_roll_number":obj.student_roll_number,
           "student_section":obj.student_section,
           "student_marks_math":obj.student_marks_math,
           "student_marks_Digital_logic":obj.student_marks_Digital_logic,
           "student_marks_programming":obj.student_marks_programming,
           "student_marks_discrete":obj.student_marks_discrete,


       }
        )
    pd.DataFrame(data).to_excel('student.xlsx')
    return JsonResponse({
        "status":200
    }) 
  

def import_data(request):
    if request.method=="POST":
        file=request.FILES["files"]
        data_import_form_excel.objects.create(
            file=file
        )
        path=file.file
        print(f"{settings.BASE_DIR}f{path}")
        df=pd.read_excel(path)
        print(df)
       
        #student.objects.create(
        #        student_name=df["student_name"],
        #        student_address=df["student_address"],
        #        student_roll_number=df["student_roll_number"],
        #        student_section=df["student_section"],
        #        student_marks_math=df["student_marks_math"],
        #        student_marks_Digital_logic=df["student_marks_Digital_logic"],
        #        student_marks_programming=df["student_marks_programming"],
        #        student_marks_discrete=df["student_marks_discrete"]
        #
                

        #  )

    return render (request,"import_data.html")




    
