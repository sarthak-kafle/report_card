from django.db import models

# Create your models here.
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
    student_marks_math=models.IntegerField()
    student_marks_Digital_logic=models.IntegerField()
    student_marks_programming=models.IntegerField()
    student_marks_discrete=models.IntegerField()
    def __str__(self):
        return self.student_name
    