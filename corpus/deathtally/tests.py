from django.test import TestCase
from deathtally.views import home_page
from django.http import HttpRequest
from django.core.urlresolvers import resolve

class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        pass

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)
