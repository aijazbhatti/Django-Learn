from django.urls import path
from . import views

urlpatterns =[
    path('shop/',views.home,name="shop-home"),
    path('product/',views.products,name="shop-home")
    
]