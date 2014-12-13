from django.shortcuts import render
from django.http import HttpResponse
#from deathtally.models import Film 
#from deathtally.models import MediaMetaData
#from deathtally.models import TimeInfo 
from deathtally.models import *
import ast

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

def add_deathtally_solution(request):
    if(request.method =="POST"):
        rpost = request.POST
        print("POOOOST " + str(rpost))
        film_ = Film.objects.get(id = rpost['ofFilm'])
        deathtallySolution_ = DeathtallySolution.objects.create(
            ofFilm = film_)
        for deathInput in rpost['deaths']:
            print("DEATH " + str(deathInput))
            event_ = Event.objects.create(
                    inMedia = film_.mediaMetaData,
                    atTimeMillis = deathInput['when'])
            death_ = Death.objects.create(
                    when=event_,
                    who=deathInput['who'])
            #death_.who = deathInput['who']
            #    data = {
            #        "ofFilm" : anaconda3.id,
            #        "deaths" : [
            #            {
            #                "who": murdoch.id,
            #                "when" : 1800000
            #            },
            #            #{
            #            #    "who": hammet.id,
            #            #    "when" : 2800000
            #            #},
            #            #{
            #            #    "who": hayes.id,
            #            #    "when" : 5900000
            #            #},
            #            ]
            #        }
        return render(request,'home.html',{'film_' : film_})
    return render(request,'home.html',{'film_' : film_})


