# Generated by Django 5.1 on 2024-11-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_student_student_marks_digital_logic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_marks_discrete',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_marks_math',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_marks_programming',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
