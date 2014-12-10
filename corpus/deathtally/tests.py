from django.test import TestCase
from deathtally.views import home_page
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from deathtally.models import Film

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        pass

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

class FilmCreateTest(TestCase):

    def test_saving_post_new_list(self):
        new_film_title = 'Happy Gilmore'
        description = 'A bumbly ex hockey player tries his hand at golf'
        response = self.client.post('/films/new', \
                data = {
                    'title' : new_film_title, 
                    'description': description,
                    'wilhelmScreamCount' : 2,
                    'minutesLength' : 70
                    }
                )
        self.assertEqual(Film.objects.count(),1)
        new_film = Film.objects.first()
        self.assertEqual(new_film.title,new_film_title)

