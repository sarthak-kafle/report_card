from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    # Your index view logic
    return render(request, 'index.html')

def login_page(request):
    # Your login page logic
    return render(request, 'login_page.html')
def regester_page(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"username is not taken ")
            return redirect ("/regester_page/")
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username

        )
        user.save()
        return redirect ("/login_page/")


    return render (request,"regester_page.html")
