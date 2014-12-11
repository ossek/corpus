from django.shortcuts import render
from django.http import HttpResponse
from deathtally.models import Film 
from deathtally.models import MediaMetaData
from deathtally.models import TimeInfo 

def home_page(request):
    return render(request,'home.html')

def new_film(request):
    media_ = MediaMetaData.objects.create( 
        title = request.POST['title'],
        description = request.POST['description'],
    )
    timeInfo_ = TimeInfo.objects.create(
        millisLength = request.POST['minutesLength'],
    )
    film_ = Film.objects.create(
        wilhelmScreamCount = request.POST['wilhelmScreamCount'],
        mediaMetaData = media_,
        timeInfo = timeInfo_
    )
    return render(request,'home.html',{'film_' : film_})

def filmsIndex(request):
    ##results per page, and page
    pass

#page that shows film and list of characters
def filmView(request):
    pass
