from django import forms
from django.conf import settings
from locations.models import Place
from users.models import myRoute

class placeForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ('coordinates',)


class myRouteForm(forms.ModelForm):
    class Meta:
        model = myRoute
        fields = ['place']
