from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return HttpResponse("Welcome to emobilis")

def about(request):
    return HttpResponse("About emobilis")

def contact(request):
    return  HttpResponse("Get in touch with emobilis now")