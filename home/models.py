from django.db import models

class regester(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=8,default="sarthak")
    def __str__(self):
        return self.username

class student(models.Model):
    student_name=models.CharField(max_length=50)
    student_address=models.CharField(max_length=100)
    student_roll_number=models.IntegerField()
    student_section=models.CharField(max_length=1)
    student_marks_math=models.IntegerField(null=True,blank=True)
    student_marks_Digital_logic=models.IntegerField(null=True,blank=True)
    student_marks_programming=models.IntegerField(null=True,blank=True)
    student_marks_discrete=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.student_name
    

#class Department(models.Model):
   # Departmant=models.CharField(max_length=50)
   # def __str__(self):
   #     return self.Departmant
class data_import_form_excel(models.Model):
     file=models.FileField(upload_to="excel")
     