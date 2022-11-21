from django.db import models

class Place(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=(('R','Restaurant'),('H','Hotel'),('A','Attraction')))
    address = models.CharField(max_length=100)
    coordinates= models.CharField(max_length=100, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    image=models.ImageField(upload_to='static/locations/images',blank=True, null=True)

    def __str__(self):
        return self.name
    
class Route(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    places= models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return self.name
    