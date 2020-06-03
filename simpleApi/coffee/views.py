from django.shortcuts import render
from django.http import JsonResponse
import json
from . import models

# Create your views here.
def index(requests):

    coffees = models.Coffee.objects.all()
    data =  list(coffees.values("id",
                                "name",
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
    

def coffedetails(requests,record_id):
    try:
        coffee = models.Coffee.objects.filter(pk=record_id)
        data = list(coffee.values("id","name","description",'price'))
        print(data)
        return JsonResponse({'response':200, 'data':data[0]})
    
    except Exception as identifier:
            
        return JsonResponse({'response':404, 'message':str(identifier)})