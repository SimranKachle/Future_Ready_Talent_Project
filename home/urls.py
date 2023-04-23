from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   
    path('',views.home3),
    path('home3/',views.home3),
    # path('home2/',views.home2),
    # path('home3/result/',views.result),
    # path('result/',views.result),
    path('home3',views.contact),
    # path('predict/',views.predict),
    
]
