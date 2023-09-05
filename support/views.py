from django.shortcuts import render

# Create your views here.
def support(request):
    return  render(request,'support.html')
def help(request):
    return render(request,'support/help.html')
def knowlegebase(request):
    return render(request,'support/knowlegebase.html')

def faq(request):
    return render(request,'support/faq.html')