from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    #Path del core
    path('', views.contact,name ="contact" ),
    
]