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

class DeathTallyMovieSearchTest(TestCase):
    # gets us title and image
    def test_movie_search_displays_html(self):
        response = self.client.get('/deathtally/solutions/moviesearch')

    #todo distinguishing film editions
    def test_next_shows_error_message_when_no_selection(self):
        pass

    def test_next_sends_data_to_character_selection(self):
        pass

class DeathTallyCharacterSelectionTest(TestCase):
    def test_character_selection_shows_actors(self):
        pass

    def test_next_sends_data_to_event_selection(self):
        pass

    def test_start_over_redirects_to_MovieSearch(self):
        pass

class DeathTallyEventSelectionTest(TestCase):
    def test_shows_characters(self):
        pass

    def test_only_allows_death_once(self):
        pass

    def test_save_creates_new_solution(self):
        pass

class DeathTallyCreateTest(TestCase):

    def setUp(self):
        # this might be a stopgap until I find 
        # a better way to setup django view functions
        # to have the dependency injected
        self.garbage = 'garbage'
    
    def test_create_new_deathtally_solution(self):
        new_film_title = "Anaconda 3"
        image_source = 'file:///projects/corpus_site/corpus/deathtally/content/image/cherries.jpg'

        postdata = {
                'filmTitle': new_film_title,
                'filmImageSrc': image_source,
                'deaths': [
                    {
                        'actorname': 'David Hasselhoff',
                        'when': 5900000,
                    },
                    {
                        'actorname': 'John Rhys Davies',
                        'when': 1800000,
                    },
                    {
                        'actorname': 'Crystal Allen',
                        'when': 800000,
                    },
                    ]
                }

        response = self.client.post('/deathtally/solutions/add', \
                data = json.dumps(postdata),content_type = 'application/json' )

        solution = DeathtallySolution.objects.first()
        self.assertEqual(solution.filmTitle,new_film_title) 
        self.assertEqual(solution.filmImageSrc,image_source)

        hammett_bleh = Death.objects.get(actorname__contains = "Hasselhoff")
        self.assertEqual(hammett_bleh.inDeathtally.id,solution.id)
        self.assertEqual(hammett_bleh.when,5900000)

        murdoch_bleh = Death.objects.get(actorname__contains = "Davies")
        self.assertEqual(murdoch_bleh.inDeathtally.id,solution.id)
        self.assertEqual(murdoch_bleh.when,1800000)

        hayes_bleh = Death.objects.get(actorname__contains = "Allen")
        self.assertEqual(hayes_bleh.inDeathtally.id,solution.id)
        self.assertEqual(hayes_bleh.when,800000)


    # test add events
    # event is not at a time later than the film's runtime
    # test duplicate actor names

    
