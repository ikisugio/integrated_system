from django.shortcuts import render

# Create your views here.

def index(name):
    print(name)
    return "is_here"