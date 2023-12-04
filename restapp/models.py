from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField()
    age=models.IntegerField()
# Create your models here.
