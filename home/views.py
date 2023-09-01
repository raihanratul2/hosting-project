from django.shortcuts import render

# Create your views here.
def home(request):
    return  render(request,'home/home.html')
def cart(request):
    return  render(request,'home/home.html')

def contact_us(request):
    return  render(request,'home/contact_us.html')

def home2(request):
    return render(request,'home/home2.html')


def home3(request):
    return render(request,'home/home3.html')


def home4(request):
    return render(request,'home/home4.html')