"""
URL configuration for report_card project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *


urlpatterns = [
       path('', index, name='home'),
    path('index/', index, name='index'),
    path('admin/', admin.site.urls),
    path("login_page/",login_page,name="login_page"),
    path("register_page/",register_page,name="register_page"),
    path("student_page/",student_page,name="student_page"),
    path("update/<int:id>",update,name="update"),
    path("result/<int:id>",result,name="result"),
    path("delete/<int:id>",delete,name="delete"),
    path("logout_page/",logout_page,name="logout_page"),
    path("piechart/",piechart,name="piechart"),
    path("data_export/",data_export,name="data_export"),
    path("import_data/",import_data,name="import_data"),
    path("report_card/<int:id>",result,name="report_card"),

    
    
]
