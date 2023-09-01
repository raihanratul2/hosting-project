from django.urls import path
from . import views
urlpatterns = [
    path('',views.services,name='services'),
    path('basic_server/',views.basic_server,name='basic_server'),
    path('resell_server/',views.resell_server,name='resell_server'),
    path('vps_server/',views.vps_server,name='vps_server'),
    path('wordpress_server/',views.wordpress_server,name='wordpress_server'),
    path('domains/',views.domains,name='domains'),
    path('dedicated_server/',views.dedicated_server,name='dedicated_server'),
    path('vps_server/',views.vps_server,name='vps_server'),
    path('ssl_service/',views.ssl_service,name='ssl_service'),

]
