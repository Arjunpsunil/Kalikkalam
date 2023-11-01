from django.shortcuts import render,redirect
from userapp.models import Location,Turf
from.models import*
import stripe
from django.conf import settings
stripe.api_key=settings.STRIPE_SECRET_KEY

def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def locations(request):
    data=Location.objects.all()
    return render(request,'locations.html',{'data':data})
def turfs(request,id):
    data=Turf.objects.filter(locationid=id,status=1)
    return render(request,'turfs.html',{'data':data})
def allturfs(request):
    data=Turf.objects.all()
    return render(request,'allturfs.html',{'data':data})
def register(request):
    return render(request,'register.html')
def registerdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        data=Register(name=name,email=email,password=password)
        data.save()
    return redirect('home')
def login(request):
    return render(request,'login.html')
def logindata(request):
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        if Register.objects.filter(name=name,password=password).exists():
           data = Register.objects.filter(name=name,password=password).values('email','id').first()
           
           request.session['ui_id'] = data['id']
           request.session['email_u'] = data['email'] 
           request.session['username_u'] = name
           request.session['password_u'] = password
           return redirect('home') 
        else:
            return render(request,'login.html',{'msg':'Invalid user credentials'})
    else:
        return redirect('login')
def logout(request):
    
    del request.session['ui_id']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def contactdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        comments=request.POST['comments']
        data=Contact(name=name,email=email,number=number,comments=comments)
        data.save()
    return redirect('home')
def checkout(request,id):
    data=Turf.objects.filter(id=id)
    data1=Turf.objects.filter(id=id)
    return render(request,'checkout.html',{'data':data,'data1':data1})
def singleturf(request,id):
    data=Turf.objects.filter(id=id)
    return render(request,'singleturf.html',{'data':data})
def checkoutdata(request):
    if request.method == 'POST':
        name=request.POST['name']
        number=request.POST['number']
        comments=request.POST['comments']
        date=request.POST['date']
        time=request.POST['time']
        userid=request.session.get('ui_id')
        turfid=request.POST['turfid']

        request.session['user_name'] = name
        request.session['user_number'] = number
        request.session['user_comments'] = comments
        request.session['user_date'] = date
        request.session['user_time'] = time
        request.session['turfs_id'] = turfid
        


        turfdetails = Turf.objects.get(id=turfid)
        session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
            line_items=[{
                    'price_data':{
                        'currency': 'inr',
                        'product_data':{
                            'name': turfdetails.name,
                        },
                        'unit_amount':int(turfdetails.price)*100,
                    
                    },
                    'quantity':1,
            }],
            mode='payment',
            success_url = "http://127.0.0.1:8000/appsuccess",
            cancel_url = "http://127.0.0.1:8000/pay_cancel",
            # client_reference_id=product_id,
        )
        return redirect(session.url, code=303)

        
    return redirect('success')

def success(request):
    userid=request.session.get('ui_id')
    user_name = request.session.get('user_name')
    user_number = request.session.get('user_number')
    user_comments = request.session.get('user_comments')
    user_date = request.session.get('user_date')
    user_time = request.session.get('user_time')
    turfid = request.session.get('turfs_id')
    data=Checkout(name=user_name,number=user_number,comments=user_comments,date=user_date,time=user_time,userid=Register.objects.get(id=userid),turfid=Turf.objects.get(id=turfid))
    data.save()
    data_1=Checkout.objects.filter(userid=userid)
    return render(request,'success.html',{'data_1':data_1})

def myorders(request):
     userid=request.session.get('ui_id')
     data=Checkout.objects.filter(userid=userid)
     return render(request,'myorders.html',{'data':data})
    
        

# Create your views here.
