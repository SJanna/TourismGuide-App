from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import placeForm, myRouteForm
from .models import Place
from users.models import myRoute

# Create your views here.

def get_place(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = placeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = placeForm()

    return render(request, 'locations/placeForm.html', {'form': form})


def list_place(request):
    places=Place.objects.all()
    myroutes=myRoute.objects.filter(user=request.user.id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if request.user.is_authenticated:
            # create a form instance and populate it with data from the request:
            form = myRouteForm(request.POST)
            for field in form:
                value= int(field.value())
            
            # check whether it's valid:
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.user = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
                obj.save() # Save the final "real form" to the DB
                added=True
                return redirect('placeList')
                # return render(request, 'locations/index.html', {'places': places, 'form': form, 'myroutes': myroutes, 'value':value, 'added':added})
            else:
                print("ERROR : Form is invalid")
                print(form.errors)
        else:
            form = myRouteForm()
            return render(request, 'locations/index.html', {'places': places, 'form': form, 'notLoged': True})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = myRouteForm()
        return render(request, 'locations/index.html', {'places': places, 'form': form, 'myroutes': myroutes})


def my_route(request):
    myplaces=myRoute.objects.filter(user=request.user.id)
    return render(request, 'locations/myRoute.html', {'myplaces':myplaces})

def place_delete(request, placeid):
    print(placeid)
    print( myRoute.objects.filter(id=placeid))
    myRoute.objects.filter(id=placeid).delete()
    print(myRoute.objects.all().values())
    return redirect('myRoute')