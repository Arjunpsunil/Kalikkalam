from django.db import models
from userapp.models import*

class Register(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    number=models.IntegerField(default=0)
    comments=models.CharField(max_length=70)
class Checkout(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField(default=0)
    date=models.DateField()
    time=models.TimeField()
    comments=models.CharField(max_length=50,default='')
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    turfid=models.ForeignKey(Turf,on_delete=models.CASCADE)
    status=models.IntegerField(default=0)




# Create your models here.
