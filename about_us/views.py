from django.shortcuts import render

# Create your views here.
def about_us(request):
    return  render(request,'about_us/about_us.html')
def terms(request):
    return  render(request,'about_us/terms.html')
def team(request):
    return  render(request,'about_us/team.html')