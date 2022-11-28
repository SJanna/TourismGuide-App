from django.shortcuts import  render, redirect, HttpResponseRedirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("placeList")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def login_request(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form=AuthenticationForm(request=request,data=request.POST)
			if form.is_valid():
				username=form.cleaned_data['username']
				psw=form.cleaned_data['password']
				user=authenticate(username=username,password=psw)
				if user is not None:
					login(request,user)
			return redirect("placeList")
		else:
			form = AuthenticationForm()
			return render(request,'registration/login.html',{'form':form})
	else:
		return redirect("placeList")
