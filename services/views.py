from django.shortcuts import render

# Create your views here.
def services(request):
    return  render(request,'services.html')


def basic_server(request):
    return  render(request,'services/basic_server.html')

def resell_server(request):
    return  render(request,'services/resell_server.html')

def dedicated_server(request):
    return  render(request,'services/dedicated_server.html')


def vps_server(request):
    return  render(request,'services/vps_server.html')


def wordpress_server(request):
    return  render(request,'services/wordpress_server.html')

def domains(request):
    return  render(request,'services/domains.html')

def ssl_service(request):
    return  render(request,'services/ssl_service.html')

