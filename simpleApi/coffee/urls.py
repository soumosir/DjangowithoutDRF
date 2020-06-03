from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.index,name="index"),
    path('<int:record_id>/',views.coffedetails,name="coffeedetails")
]