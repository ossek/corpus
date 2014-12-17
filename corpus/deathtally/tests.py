from django.test import TestCase
from deathtally.views import home_page
from django.http import HttpRequest
from django.core.urlresolvers import resolve
#from deathtally.models import Film
from deathtally.models import *
import json

# todo something is needed to setup the view functions ahead of time
# cheap way could be to pass the external service function as an optional
# param directly to the view


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        pass

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

class DeathTallyCreateTest(TestCase):

    def setUp(self):
        # this might be a stopgap until I find 
        # a better way to setup django view functions
        # to have the dependency injected
        self.garbage = 'garbage'

    def test_creating_new_game_solution(self):
        ##make the movie
        title = "anaconda 3 deathtally"
        new_film_title = "Anaconda 3"
        description = "Hasselhoff in the jungle"

        response = self.client.post('/films/add', \
                data = {
                    'title' : new_film_title, 
                    'description': description,
                    'wilhelmScreamCount' : 15,
                    'minutesLength' : 70,
                    'tmdbFilmId' : 1
                    }
                )

        anaconda3 = Film.objects.first()

        #actors (don't exist yet)
        hassel = Actor.objects.create(
                person = Person.objects.create(realName = "David Hasselhoff"),
                tmdbPersonId = 1)
        crys =  Actor.objects.create(
                person = Person.objects.create(realName = "Crystal Allen"),
                tmdbPersonId = 2)
        john = Actor.objects.create(
                person = Person.objects.create(realName = "John Rhys Davies"),
                tmdbPersonId = 3)

        #characters (don't exist yet)
        hammett = Character.objects.create(actor = hassel,
                inMedia = anaconda3.mediaMetaData,
                tmdbCreditId = 1,
                characterName = "Markos Hammett")
        hayes = Character.objects.create(actor = crys,
                inMedia = anaconda3.mediaMetaData,
                tmdbCreditId = 2,
                characterName = 'Dr. Amanda Hayes')
        murdoch = Character.objects.create(actor = john,
                inMedia = anaconda3.mediaMetaData,
                tmdbCreditId = 3,
                characterName = 'Murdoch')

        ##this is the bit done by user interaction
        #make the game solution
        gameSolution =  DeathtallySolution()
        gameSolution.mediaMetaData = anaconda3.mediaMetaData

        postdata = {
                    "ofFilm" : anaconda3.id,
                    "deaths" : [
                        {
                            "who": hammett.id,
                            "when" : 2800000
                        },
                        {
                            "who": hayes.id,
                            "when" : 5900000
                        },
                        {
                            "who": murdoch.id,
                            "when" : 1800000
                        },
                        ]
                    }

        response = self.client.post('/deathtally/add', \
                data = json.dumps(postdata),content_type = 'application/json' )
        
        #deaths
        solution = DeathtallySolution.objects.first()

        #murdoch_bleh = Death.objects.first()
        hammett_bleh = Death.objects.get(who__characterName__contains = "Hammett")
        self.assertEqual(hammett_bleh.inDeathtally.id,solution.id)
        self.assertEqual(hammett_bleh.when.atTimeMillis,2800000)
        self.assertEqual(hammett_bleh.when.inMedia.id,anaconda3.mediaMetaData.id)

        hayes_bleh = Death.objects.get(who__characterName__contains = "Hayes")
        self.assertEqual(hayes_bleh.inDeathtally.id,solution.id)
        self.assertEqual(hayes_bleh.when.atTimeMillis,5900000)
        self.assertEqual(hayes_bleh.when.inMedia.id,anaconda3.mediaMetaData.id)

        murdoch_bleh = Death.objects.filter(who__characterName = "Murdoch").first()
        self.assertEqual(murdoch_bleh.inDeathtally.id,solution.id)
        self.assertEqual(murdoch_bleh.when.atTimeMillis,1800000)
        self.assertEqual(murdoch_bleh.when.inMedia.id,anaconda3.mediaMetaData.id)

class test_Get_Movies_For_GameSolution_SearchResults(TestCase):
    pass
    
