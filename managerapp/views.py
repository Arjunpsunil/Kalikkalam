from django.shortcuts import render,redirect
from.models import*
from userapp.models import*
from app.models import*

def managerbase(request):
    return render(request,'managerbase.html')
def manreg(request):
    return render(request,'manreg.html')
def manregdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        password=request.POST['password']
        data=Managerdata(name=name,email=email,number=number,password=password)
        data.save()
    return redirect('manhome')
def manhome(request):
    data=Turf.objects.all()
    return render(request,'manhome.html',{'data':data})
def manturf(request,id):
    data=Turf.objects.filter(managerid=id,status=0)
    return render(request,'manturf.html',{'data':data})
def manapprove(request,id):
    data=Turf.objects.filter(id=id).update(status=1)
    return redirect('apmanturf')
def delmanturf(request,id):
    data=Turf.objects.filter(id=id).update(status=2)
    return redirect('apmanturf')
def apmanturf(request):
    data=Turf.objects.filter(status=1)
    data1=Turf.objects.filter(status=2)
    return render(request,'apmanturf.html',{'data':data,'data1':data1})
def bookingap(request,id):
    data=Checkout.objects.filter(turfid=Turf.objects.get(managerid=id),status=0)
    return render(request,'bookingap.html',{'data':data})
def bookapprove(request,id):
    data=Checkout.objects.filter(id=id).update(status=1)
    return redirect('appbook')
def delbook(request,id):
    data=Checkout.objects.filter(id=id).update(status=2)
    return redirect('appbook')
def appbook(request):
    data=Checkout.objects.filter(status=1)
    data1=Checkout.objects.filter(status=2)
    return render(request,'appbook.html',{'data':data,'data1':data1})



# Create your views here.
