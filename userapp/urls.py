from django.urls import path
from.import views

urlpatterns = [
    path('',views.addlocation,name='addlocation'),
    path('location',views.location,name='location'),
    path('locationtable',views.locationtable,name='locationtable'),
    path('addturf',views.addturf,name='addturf'),
    path('turf',views.turf,name='turf'),
    path('turftable',views.turftable,name='turftable'),
    path('registertable',views.registertable,name='registertable'),
    path('contacttable',views.contacttable,name='contacttable'),
    path('checkouttable',views.checkouttable,name='checkouttable'),
    path('userhome',views.userhome,name='userhome'),
    path('mantable',views.mantable,name='mantable'),
    path('man/<int:id>/',views.man,name='man'),
    path('approvedman',views.approvedman,name='approvedman'),
    path('mandel/<int:id>/',views.mandel,name='mandel'),
    path('counttable',views.counttable,name='counttable')



    
]
