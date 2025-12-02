from django.contrib import admin
from .views import home,about
from django.urls import path

urlpatterns = [
    path('', home, name='blog3-home'),   
    path('about/', about, name='blog3-home')  
]