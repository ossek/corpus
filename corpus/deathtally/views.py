from django.shortcuts import render
from django.http import HttpResponse
from deathtally.models import Film 

def home_page(request):
    return render(request,'home.html')

def new_film(request):
    film_ = Film.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        minutesLength = request.POST['minutesLength'],
        wilhelmScreamCount = request.POST['wilhelmScreamCount'])
    return render(request,'home.html',{'film_' : film_})




