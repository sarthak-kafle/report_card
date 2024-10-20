from django.db import models

# Create your models here.
class regester(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=10)
    def __str__(self):
        return self.username