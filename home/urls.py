from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home2/',views.home2,name='home2'),
    path('home3/',views.home3,name='home3'),
    path('home4/',views.home4,name='home4'),
    path('cart/',views.cart,name='cart'),
    path('contact/',views.contact_us,name='contact_us'),

]
