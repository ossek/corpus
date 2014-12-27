from deathtally.apiviews import movieSearch
from deathtally.apimodels import MovieSearchResult
from unittest import patch
#from unittest import TestCase
from django.test import TestCase

class WhenApiGivesNoResultTest(TestCase):

    def test_somthing(self):
        self.assertEqual('b','n')

    @patch.object('tmdbsimple.search.Search')
    def test_thenEmptyArrayReturned(self,stubbedSearchClass):
        stubbedSearch = stubbedSearchClass.return_value
        stubbedSearch.movie.return_value = {'page': 1, 'results': [], 'total_pages': 0, 'total_results': 0} 
        searchResult = movieSearch.searchByTitle('some title with no results')
        self.assertEqual(searchResult,1)


class WhenApiReturnsResult(TestCase):

    def test_thenMovieSearchResultReturned(self):
        pass

    def test_thenFilmTitleIsCorrect(self):
        pass

    def test_thenImagePathIsCorrect(self):
        pass

class WhenApiGivesMoreThanOneResult(TestCase):
    
    def test_thenSameCountOfResultModelsReturned(self):
        pass

#result = MovieSearchResult(self)
#  result.filmTitle="Star Wars"
#  result.filmImageSrc="https://image.tmdb.org/t/p/w154/ghd5zOQnDaDW1mxO7R5fXXpZMu.jpg"
#  result2 = MovieSearchResult(self)
#  result2.filmTitle="Pride and Prejudice"
#  result2.filmImageSrc="https://image.tmdb.org/t/p/w154/AukVKsjZOVR2CBfI3vSJRXNLEKr.jpg"
#  results = [result,result2]
#
