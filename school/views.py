from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def welcome(request):
    return render(request,'welcome.html')