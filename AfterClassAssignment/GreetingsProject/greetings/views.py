from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    # return HttpResponse("Welcome to the Greetings App!")
    return render(request,'welcome.html')

def greet(request, username):
    # return HttpResponse(f"Hello, {username}!")
    return render(request,'greet.html',{'username':username,'age':23})

def farewell(request, username):
    # return HttpResponse(f"Goodbye, {username}!")
    return render(request,'farewell.html',{'username':username})
