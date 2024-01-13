from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from pprint import pprint

# Create your views here.

 
def index(request):
     destinations = Destination.objects.all()
     dd(destinations)

     return render(request, 'index.html',{ 'destinations': destinations })

