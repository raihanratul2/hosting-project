from django.urls import path 
from . import views

urlpatterns = [
    path('',views.support,name='support'),
    path('help/',views.help,name='help'),
    path('knowlegebase/',views.knowlegebase,name='knowlegebase'),
    path('faq/',views.faq,name='faq'),
]