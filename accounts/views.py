from django.shortcuts import render

# Create your views here.


def register(request):
    return  render(request,'register.html')

def signin(request):
    return render(request,'signin.html')






