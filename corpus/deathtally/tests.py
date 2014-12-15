from django.test import TestCase
from deathtally.views import home_page
from django.http import HttpRequest
from django.core.urlresolvers import resolve
#from deathtally.models import Film
from deathtally.models import *
import json

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
        hassel =  Person.objects.create()
        hassel.realName = "David Hasselhoff"
        john = Person.objects.create()
        john.realName = "John Rhys Davies"
        crys =  Person.objects.create()
        crys.realName = "Crystal Allen"

        #characters
        hammett = Character.objects.create(person = hassel,
                inMedia = anaconda3.mediaMetaData,
                characterName = "Markos Hammett")
        hayes = Character.objects.create(person = crys,
                inMedia = anaconda3.mediaMetaData,
                characterName = 'Dr. Amanda Hayes')
        murdoch = Character.objects.create(person = john,
                inMedia = anaconda3.mediaMetaData,
                characterName = 'Murdoch')

        ##this is the bit done by user interaction
        #make the game solution
        gameSolution =  DeathtallySolution()
        gameSolution.mediaMetaData = anaconda3.mediaMetaData

        postdata = {
                    "ofFilm" : anaconda3.id,
                    "deaths" : [
                        {
                            "who": murdoch.id,
                            "when" : 1800000
                        },
                        {
                            "who": hammett.id,
                            "when" : 2800000
                        },
                        {
                            "who": hayes.id,
                            "when" : 5900000
                        },
                        ]
                    }

        response = self.client.post('/deathtally/add', \
                data = json.dumps(postdata),content_type = 'application/json' )
        
        #deaths
        solution = DeathtallySolution.objects.first()

        #murdoch_bleh = Death.objects.first()
        murdoch_bleh = Death.objects.filter(who__characterName = "Murdoch").first()
        print('murdoch bleh name ' + str(murdoch_bleh.who.characterName))
        self.assertEqual(murdoch_bleh.inDeathtally.id,solution.id)
        self.assertEqual(murdoch_bleh.when.atTimeMillis,1800000)
        self.assertEqual(murdoch_bleh.when.inMedia.id,anaconda3.mediaMetaData.id)

        hammett_bleh = Death.objects.get(who__characterName__contains = "Hammett")
        self.assertEqual(hammett_bleh.inDeathtally.id,solution.id)
        self.assertEqual(hammett_bleh.when.atTimeMillis,2800000)
        self.assertEqual(hammett_bleh.when.inMedia.id,anaconda3.mediaMetaData.id)

        hayes_bleh = Death.objects.get(who__characterName__contains = "Hayes")
        self.assertEqual(hayes_bleh.inDeathtally.id,solution.id)
        self.assertEqual(hayes_bleh.when.atTimeMillis,5900000)
        self.assertEqual(hayes_bleh.when.inMedia.id,anaconda3.mediaMetaData.id)

        
