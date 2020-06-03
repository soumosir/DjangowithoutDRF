from django.db import models


# Create your models here.

class Coffee(models.Model):

    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    quantity = models.IntegerField()
    caffeine = models.IntegerField()
    milk = models.IntegerField()
    water = models.IntegerField()
    sugar = models.IntegerField()
    temperature = models.CharField(max_length=256)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name