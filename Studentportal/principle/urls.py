from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('addteacher',views.addteacher1, name='loginpage'),
    
    path('addstudent', views.addstudent, name="addstudent"),
    path('addstudent_registerd_cources', views.addstudent_registerd_cources, name="views.addstudent_registerd_cources"),
    path('createteacher', views.createteacher, name="createteacher"),
     path('addstudent1', views.addstudent1, name="addstudent1"),
     path('addsubject', views.addsubject, name="addstudent"),
     path('addsubject1', views.addsubject1, name="addstuden1t"),

  
]
