from django.urls import path
from.import views

urlpatterns = [
    path('',views.base,name='base'),
    path('home',views.home,name='home'),
    path('locations',views.locations,name='locations'),
    path('turfs/<int:id>/',views.turfs,name='turfs'),
    path('allturfs',views.allturfs,name='allturfs'),
    path('register',views.register,name='register'),
    path('registerdata',views.registerdata,name='registerdata'),
    path('login',views.login,name='login'),
    path('logindata',views.logindata,name='logindata'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('contactdata',views.contactdata,name='contactdata'),
    path('checkout/<int:id>/',views.checkout,name='checkout'),
    path('singleturf/<int:id>/',views.singleturf,name='singleturf'),
    path('checkoutdata',views.checkoutdata,name='checkoutdata'),
    path('success',views.success,name='success'),
    path('myorders',views.myorders,name='myorders')

   
   

    
]