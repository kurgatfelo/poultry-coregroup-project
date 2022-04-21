from django.shortcuts import render,redirect
from django.http.response import Http404
from rest_framework import generics
from django.http  import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from poultryapp.models import Diseases,User,Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    diseases = Diseases.objects.all()
    users = User.objects.all()
    return render(request, 'homepage.html', {"diseases":diseases, "users": users})

def search_results(request):
    if 'disease' in request.GET and request.GET["disease"]:
        search_term = request.GET.get("disease")
        searched_diseases = Diseases.search_project(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message,"diseases": searched_diseases})
    else:
        message = "You haven't searched for any diseases yet"
    return render(request, 'search.html', {'message': message})