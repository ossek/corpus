from deathtally.service.external.tmdb.movieCredits import getCast
from deathtally.apimodels import MovieSearchResult
from unittest import mock
from unittest import TestCase
import requests

class WhenGetCastGivesNoResultTest(TestCase):

    def setUp(self):
        patcher = mock.patch('tmdbsimple.movies.Movies',autospec=True)
        stubbedMovieClass = patcher.start()
        stubbedMovie = stubbedMovieClass.return_value
        stubbedMovie.credits.return_value = {'cast':[]}
        self.addCleanup(patcher.stop)

    def test_thenEmptyArrayReturned(self):
        result = getCast(999)
        self.assertEqual(result,[])

class WhenGetCastGivesResultTest(TestCase):

    def setUp(self):
        patcher = mock.patch('tmdbsimple.movies.Movies',autospec=True)
        stubbedMovieClass = patcher.start()
        stubbedMovie = stubbedMovieClass.return_value
        stubbedMovie.credits.return_value = {'cast':[
            {
                'cast_id': 1,
                'character': 'Terri Flores',
                'credit_id': '52fe44edc3a36847f80b2529',
                'id': 16866,
                'name': 'Jennifer Lopez',
                'order': 0,
                'profile_path': '/hNgmDBICnD8La2QN1Pkflh5NJqJ.jpg' 
            }]}
        self.addCleanup(patcher.stop)

    def test_thenOneResultIsReturned(self):
        result = getCast(1)
        self.assertEqual(len(result),1)

    def test_thenImageUrlIsCorrect(self):
        result = getCast(1)
        self.assertEqual(result[0]['filmImgSrc'],'https://image.tmdb.org/t/p/w92/hNgmDBICnD8La2QN1Pkflh5NJqJ.jpg')

    def test_thenTmdbPropertiesAreCorrect(self):
        result = getCast(1)
        self.assertEqual
        self.assertEqual(result[0]['cast_id'], 1)
        self.assertEqual(result[0]['character'], 'Terri Flores')
        self.assertEqual(result[0]['credit_id'], '52fe44edc3a36847f80b2529')
        self.assertEqual(result[0]['id'], 16866)
        self.assertEqual(result[0]['name'], 'Jennifer Lopez')
        self.assertEqual(result[0]['order'], 0)
        self.assertEqual(result[0]['profile_path'], '/hNgmDBICnD8La2QN1Pkflh5NJqJ.jpg' )
