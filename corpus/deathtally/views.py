from django.shortcuts import render
from django.http import HttpResponse
#from deathtally.models import Film 
#from deathtally.models import MediaMetaData
#from deathtally.models import TimeInfo 
from deathtally.models import *
import json

def home_page(request):
    return render(request,'home.html')

def add_film(request):
    if(request.method == "POST"):
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
    return render(request,'add_film.html')

def film_index(request):
    ##results per page, and page
    pass

#page that shows film and list of characters
def film_info(request):
    if(request.method == "POST"):
        pass
    pass

#assume we're going to get json in the post
def add_deathtally_solution(request):
    if(request.method =="POST"):
        data = json.loads(bytes.decode(request.body))
        film_ = Film.objects.get(id = data['ofFilm'])
        deathtallySolution_ = DeathtallySolution.objects.create(
            ofFilm = film_)
        for deathInput in data['deaths']:
            print('DEATH INPUT ' + str(deathInput))
            event_ = Event.objects.create(
                    inMedia = film_.mediaMetaData,
                    atTimeMillis = deathInput['when'])
            character = Character.objects \
                    .get(id=deathInput['who'])
            death_ = Death.objects.create(
                    when=event_,
                    who= character,
                    inDeathtally = deathtallySolution_)
        return render(request,'home.html',{'film_' : film_})
    return render(request,'home.html',{'film_' : film_})


