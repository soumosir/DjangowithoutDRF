from django.test import TestCase

from . import models
# Create your tests here.



class CoffeeTestCase(TestCase):
    def setUp(self):
        pass

    def test_coffee_db(self):
        
        
        coffee = models.Coffee.objects.filter(pk=1)
        data = list(coffee.values("id","name","description",'price'))
        
        real_value =  [{
            "id": 1,
            "name": "Arabica",
            "description": "Finest Coffee from the West",
            "price": 200
        }]
        
        self.assertEqual(data, real_value)

    def test_coffee_db2(self):
        coffee = models.Coffee.objects.filter(pk=1)
        data = list(coffee.values("id","name","description",'price'))
        
        real_value =  [{
            "id": 1,
            "name": "Arabica",
            "description": "Finest Coffee from the West",
            "price": 200
        }]
        
        self.assertEqual(data, real_value)