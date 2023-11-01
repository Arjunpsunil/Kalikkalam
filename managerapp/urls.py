from django.urls import path
from.import views

urlpatterns = [
   path('',views.manreg,name='manreg'),
   path('managerbase',views.managerbase,name='managerbase'),
   path('manregdata',views.manregdata,name='manregdata'),
   path('manhome',views.manhome,name='manhome'),
   path('manturf/<int:id>/',views.manturf,name='manturf'),
   path('manapprove/<int:id>/',views.manapprove,name='manapprove'),
   path('delmanturf/<int:id>/',views.delmanturf,name='delmanturf'),
   path('apmanturf',views.apmanturf,name='apmanturf'),
   path('bookingap/<int:id>/',views.bookingap,name='bookingap'),
   path('bookapprove/<int:id>/',views.bookapprove,name='bookapprove'),
   path('delbook/<int:id>/',views.delbook,name='delbook'),
   path('appbook',views.appbook,name='appbook')
   
   

   
    
]