from django.shortcuts import render
from django.http import HttpResponse
#from deathtally.models import Film 
#from deathtally.models import MediaMetaData
#from deathtally.models import TimeInfo 
from deathtally.models import *
import json

def home_page(request):
    return render(request,'home.html')

def play_a_deathtally(request):
    pass

#page that shows film and list of characters
def deathtally_solution_index(request):
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


