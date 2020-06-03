from django.shortcuts import render
from django.http import JsonResponse
import json
from . import models

# Create your views here.
def index(requests):

    coffees = models.Route.objects.all()
    data =  list(coffees.values("name",
                                "description",
                                "price",
                                "quantity",
                                "caffeine",
                                "milk",
                                "water",
                                "sugar",
                                "temperature",
                                "country"))
    return JsonResponse({'response':200, 'data':data})
    
