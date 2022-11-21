from django.contrib import admin
from users.models import myRoute
from locations.models import Route, Place
# Register your models here.

admin.site.register(myRoute)
admin.site.register(Place)
admin.site.register(Route)

