from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Olha, se você não me ama</h1><h2>Caneta azul, azul caneta</h2>")