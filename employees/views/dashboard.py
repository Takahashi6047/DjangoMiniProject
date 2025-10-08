from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("<h1>Welcome to Employees Dashboard</h1><p>This is the employees page.</p>")