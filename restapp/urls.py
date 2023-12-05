from django.urls import path
from.import views

urlpatterns = [
   # path('getdata',views.getdata,name='getdata'),
   # path('update/<int:id>/',views.update,name='update'),
   path('Studentapiview',views.Studentapiview.as_view(),name='Studentapiview'),
   path('Studentupdate/<int:id>/',views.Studentupdate.as_view(),name='Studentupdate')


   
   

   
    
]