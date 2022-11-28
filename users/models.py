from django.db import models
from locations.models import Place
from django.contrib.auth.models import User


class myRoute(models.Model):
    id = models.BigAutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    place= models.ForeignKey(Place, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.place.name

