from unicodedata import name
from django import views
from django.urls import include,path
from .import views

urlpatterns = [
    path('',views.home,name='reg'), 

    path('usercreate',views.usercreate,name="usercreate"),
]