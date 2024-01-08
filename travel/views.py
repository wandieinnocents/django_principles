from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.


def index(request):
     destination1 = Destination();
     destination2 = Destination();
     destination3 = Destination();
     destination4 = Destination();

    #  destination one
     destination1.name = 'Mumbai'
     destination1.price = 500
     destination1.description = "This is one of the best city"

    #  destination two
     destination2.name = 'Kampala'
     destination2.price = 200
     destination2.description = "another is one of the best city"

      #  destination three
     destination3.name = 'Gulu'
     destination3.price = 45
     destination3.description = "Gulu is one of the best city"

     #  destination four
     destination4.name = 'Kirekaa'
     destination4.price = 45
     destination4.description = "kireka is one of the best city"

    #  create one object
     destinations = [destination1,destination2, destination3,destination4]
     

     return render(request, 'index.html',{ 'destinations': destinations })

