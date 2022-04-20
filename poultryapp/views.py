from django.shortcuts import render
from poultryapp.models import Comments,Profile,Disease
from django.shortcuts import render,redirect
# Create your views here.
def homepage(request):
    message = 'welcome to poultry farmers'
    # disease = Disease.objects.all()
    # user = User.objects.all()
    return render(request,'homepage.html',{'message':message})
def profile(request):
    message= 'welcome to proifile'
    return render(request,'profile.html',{'message':message})
def disease(request):
    message = "Diseases"
    return render(request,'new_disease.html',{'message':message})
def search_results(request):
    message = "Search"
    return render(request,'search.html',{'message':message})
def update_profile(request):
    message = "Update"
    return render(request,'search.html',{'message':message})
def upload_disease(request):
    message = "Upload"
    return render(request,'new_disease.html',{'message':message})
def comments(request):
    message = "Comments"
    return render(request,'new_comments.html',{'message':message})


