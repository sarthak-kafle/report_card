# Generated by Django 5.1 on 2024-10-21 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_addresh',
            new_name='student_address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_marks_programing',
            new_name='student_marks_programming',
        ),
    ]
