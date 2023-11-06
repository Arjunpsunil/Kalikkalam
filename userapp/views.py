from django.shortcuts import render,redirect
from.models import*
from app.models import Register,Contact,Checkout
from managerapp.models import Managerdata
import stripe

def addlocation(request):
    return render(request,'addlocation.html')
def location(request):
    if request.method =='POST':
        name=request.POST['name']
        image=request.FILES['image']
        data=Location(name=name,image=image)
        data.save()
    return redirect('locationtable')
def locationtable(request):
    data=Location.objects.all()
    return render(request,'locationtable.html',{'data':data})
def addturf(request):
    data=Location.objects.all()
    data1=Managerdata.objects.filter(status=1)
    return render(request,'addturf.html',{'data':data,'data1':data1})
def turf(request):
    if request.method=='POST':
        name=request.POST['name']
        image=request.FILES['image']
        description=request.POST['description']
        price=request.POST['price']
        location=request.POST['location']
        manager=request.POST['manager']
        data=Turf(name=name,image=image,description=description,price=price,locationid=Location.objects.get(id=location),managerid=Managerdata.objects.get(id=manager))
        data.save()
    return redirect('turftable')
def turftable(request):
    data=Turf.objects.all()
    return render(request,'turftable.html',{'data':data})
def registertable(request):
    data=Register.objects.all()
    return render(request,'registertable.html',{'data':data})
def contacttable(request):
    data=Contact.objects.all()
    return render(request,'contacttable.html',{'data':data})
def checkouttable(request):
    data=Checkout.objects.all()
    return render(request,'checkouttable.html',{'data':data})
def userhome(request):
    return render(request,'userhome.html')
def mantable(request):
    data=Managerdata.objects.filter(status=0)
    return render(request,'mantable.html',{'data':data})
def man(request,id):
    data=Managerdata.objects.filter(id=id).update(status=1)
    return redirect('approvedman')
def approvedman(request):
    data=Managerdata.objects.filter(status=1)
    data1=Managerdata.objects.filter(status=2)
    return render(request,'approvedman.html',{'data':data,'data1':data1})
def mandel(request,id):
    data=Managerdata.objects.filter(id=id).update(status=2)
    return redirect('approvedman')
def counttable(request):
    turfs=Turf.objects.all().count()
    locations=Location.objects.all().count()
    register=Register.objects.all().count()
    manager=Managerdata.objects.all().count()
    checkout=Checkout.objects.all().count()
    return render(request,'counttable.html',{'turfs':turfs,'locations':locations,'register':register,'manager':manager,'checkout':checkout})
    


# Create your views here.
