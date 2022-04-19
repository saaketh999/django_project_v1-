from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request,'webapp/welcome.html')
def menu(request):
    return render(request,'webapp/menu.html')
