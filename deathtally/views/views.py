from django.shortcuts import render
from django.http import HttpResponse
#from deathtally.models import Film 
#from deathtally.models import MediaMetaData
#from deathtally.models import TimeInfo 
from deathtally.models import *
import json

def home_page(request):
    return render(request,'home.html')

def deathtally_solution_index(request):
    pass

def moviesearch(request):
    if(request.method == "GET"):
        return render(request,'moviesearch.html')

def createsolution(request,tmdbMovieId):
    if(request.method == "GET"):
        return render(request,'makesolution.html',{'tmdbMovieId': tmdbMovieId})

#assume we're going to get json in the post
def add_deathtally_solution(request):
    if(request.method =="POST"):
        data = json.loads(bytes.decode(request.body))
        deathtallySolution_ = DeathtallySolution.objects.create(
              filmTitle = data['filmTitle'],
              filmImageSrc = data['filmImageSrc']
            )
        for deathInput in data['deaths']:
            print('DEATH INPUT ' + str(deathInput))
            death_ = Death.objects.create(
                    actorname = deathInput['actorname'],
                    when = deathInput['when'],
                    inDeathtally = deathtallySolution_)
        return render(request,'home.html',{'deathtallySolution_' : deathtallySolution_})
    return render(request,'home.html',{'deathtallySolution_' : deathtallySolution_})
