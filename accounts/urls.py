from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('register/',views.register,name='register'),
    path('services/',views.services,name='services'),
    path('basic_server/',views.basic_server,name='basic_server'),
    path('basic_server/',views.basic_server,name='basic_server'),
    path('vps_server/',views.vps_server,name='vps_server'),
    path('wordpress_server/',views.wordpress_server,name='wordpress_server'),
    path('domains/',views.domains,name='domains'),
    path('cart/',views.cart,name='cart'),
    path('home2/',views.home2,name='home2'),
    path('home3/',views.home3,name='home3'),
    path('home4/',views.home4,name='home4'),
    path('dedicated_server/',views.dedicated_server,name='dedicated_server'),
    path('vps_server/',views.vps_server,name='vps_server'),
    path('ssl_service/',views.ssl_service,name='ssl_service'),
    path('team/',views.team,name='team'),
    path('/',views.home,name='home'),
    path('/',views.home,name='home'),
    path('/',views.home,name='home'),
    
    
    

]
