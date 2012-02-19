# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from models import UserProfile
from django.db import IntegrityError

def create_user(request):
    #username = request.GET['username']
    #password = request.GET['password']
    username = request.POST['username']
    password = request.POST['password']
    try:
        newUser = User.objects.create_user(username, username, password)
        return HttpResponse("Account succesfully created");
    except IntegrityError:
        return HttpResponse("Account creation failed");

def authenticate_user(request):
    name = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username=name, password=passw)
    if user is not None:
        if user.is_active:
            return HttpResponse("Succesful authentication")
        else:
            return HttpResponse("Your account has been disabled")
    else:
        return HttpResponse("Your username or password was invalid")
