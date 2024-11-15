from faker import Faker
import random
from .models import *
fake=Faker()
def data(n=10)->None:
    try:
       for _ in range(n):
      
          student_name=fake.name()
          student_address=fake.address()
          student_section = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
          student_roll_number=random.randint(1,100)
          student_marks_Digital_logic=random.randint(40,100)
          student_marks_math=random.randint(40,100)
          student_marks_programming=random.randint(40,100)
          student_marks_discrete=random.randint(40,100)
          while student.objects.filter(student_roll_number=student_roll_number).exists():
             student_roll_number=random.randint(1,100)
          student.objects.create(
             student_name=student_name,
             student_address=student_address,
             student_roll_number=student_roll_number,
             student_marks_Digital_logic=student_marks_Digital_logic,
             student_marks_math=student_marks_math,
             student_marks_programming=student_marks_programming,
             student_marks_discrete=student_marks_discrete,
             student_section=student_section,
            )
             
          
             
                  
      
    except Exception as error:
       print(f"{error}")
