from django.db import models


class Managerdata(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.IntegerField(default=0)
    password=models.CharField(max_length=20)
    status=models.IntegerField(default=0)
    


# Create your models here.
