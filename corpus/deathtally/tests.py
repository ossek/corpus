from django.test import TestCase
from deathtally.views import home_page
from django.http import HttpRequest
from django.core.urlresolvers import resolve
#from deathtally.models import Film
from deathtally.models import *

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        pass

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

class FilmCreateTest(TestCase):

    def test_saving_post_new_film(self):
        new_film_title = 'Happy Gilmore'
        description = 'A bumbly ex hockey player tries his hand at golf'
        response = self.client.post('/films/add', \
                data = {
                    'title' : new_film_title, 
                    'description': description,
                    'wilhelmScreamCount' : 2,
                    'minutesLength' : 70
                    }
                )
        self.assertEqual(Film.objects.count(),1)
        new_film = Film.objects.first()
        self.assertEqual(new_film.mediaMetaData.title,new_film_title)
        self.assertEqual(new_film.mediaMetaData.description,description)

class DeathTallyCreateTest(TestCase):

    def test_creating_new_game_solution(self):
        title = "anaconda 3 deathtally"
        ##make the movie
        new_film_title = "Anaconda 3"
        description = "Hasselhoff in the jungle"

        response = self.client.post('/films/add', \
                data = {
                    'title' : new_film_title, 
                    'description': description,
                    'wilhelmScreamCount' : 15,
                    'minutesLength' : 70
                    }
                )

        anaconda3 = Film.objects.first()

        #actors
        #hassel =  Person()
        #hassel.realName = "David Hasselhoff"
        john = Person.objects.create()
        john.realName = "John Rhys Davies"
        #crys =  Person()
        #crys.realName = "Crystal Allen"

        #characters
        #hammett =  Character()
        #hammett.inMedia = anaconda3.mediaMetaData
        #person = hassel
        #characterName = "Markos Hammett"
        #hayes =  Character()
        #hayes.inMedia = anaconda3.mediaMetaData
        #person = crys
        #characterName = "Dr. Amanda Hayes"
        murdoch = Character.objects.create(person = john,inMedia = anaconda3.mediaMetaData)
        characterName = "Murdoch"

        ##this is the bit done by user interaction
        #make the game solution
        gameSolution =  DeathtallySolution()
        gameSolution.mediaMetaData = anaconda3.mediaMetaData

        response = self.client.post('/deathtally/add', \
                data = {
                    "ofFilm" : anaconda3.id,
                    "deaths" : [
                        {
                            "who": murdoch.id,
                            "when" : 1800000
                        },
                        #{
                        #    "who": hammet.id,
                        #    "when" : 2800000
                        #},
                        #{
                        #    "who": hayes.id,
                        #    "when" : 5900000
                        #},
                        ]
                    }
        )
        
        #deaths
        solution = DeathtallySolution.objects.first()
        murdoch_bleh = Death.objects.first()
        #murdoch_bleh = Death.objects.get(who.characterName = "murdoch")
        self.assertEqual(murdoch_bleh.inDeathtally.id,solution.id)
        self.assertEqual(murdoch_bleh.when.atTimeMillis,1800000)
        self.assertEqual(murdoch_bleh.when.inMedia.id,anaconda3.mediaMetaData.id)

        #hammet_bleh =  Death()
        #hammet_bleh.inDeathtally = gameSolution
        #hammet_bleh.who = hammet
        #hammet_bleh.when =  Event()
        #hammet_bleh.when.inMedia = anaconda3.mediaMetaData
        #hammet_bleh.when.atTimeMillis = 2800000
        #hammet_bleh.when.name = "ded"

        #hayes_bleh =  Death()
        #hayes_bleh.inDeathtally = gameSolution
        #hayes_bleh.who = hayes
        #hayes_bleh.when =  Event()
        #hayes_bleh.when.inMedia = anaconda3.mediaMetaData
        #hayes_bleh.when.atTimeMillis = 5900000
        #hayes_bleh.when.name = "ded"


