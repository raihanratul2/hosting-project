from django.urls import path
from . import views

urlpatterns = [
    path('',views.about_us,name='about_us'),
    path('terms/',views.terms,name='terms'),
    path('team/',views.team,name='team'),

]
