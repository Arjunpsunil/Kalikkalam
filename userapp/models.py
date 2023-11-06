from django.db import models
from managerapp.models import Managerdata


class Location(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='image',default='null.jpg')
class Turf(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='image',default='null.jpg')
    description=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    locationid=models.ForeignKey(Location,on_delete=models.CASCADE)
    managerid=models.ForeignKey(Managerdata,on_delete=models.CASCADE,null=True)
    status=models.IntegerField(default=0)

