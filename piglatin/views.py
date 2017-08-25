from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    request.GET["originaltext"]
    return HttpResponse("You're on the translate page!" + request.GET["originaltext"])
