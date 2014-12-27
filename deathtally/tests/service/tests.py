from deathtally.service.external.tmdb.movieSearch import searchByTitle
from deathtally.apimodels import MovieSearchResult
from unittest import mock
from unittest import TestCase

class WhenApiGivesNoResultTest(TestCase):

    @mock.patch('tmdbsimple.search.Search')
    def test_thenEmptyArrayReturned(self,stubbedSearchClass):
        stubbedSearch = stubbedSearchClass.return_value
        stubbedSearch.movie.return_value = {'page': 1, 'results': [], 'total_pages': 0, 'total_results': 0} 
        searchResult = searchByTitle('some title with no results')
        self.assertEqual(searchResult,[])

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
