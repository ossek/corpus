from deathtally.service.external.tmdb.movieSearch import searchByTitle
from deathtally.apimodels import MovieSearchResult
from unittest import mock
from unittest import TestCase
import requests

class WhenApiMovieSearchGivesNoResultTest(TestCase):

    def setUp(self):
        patcher = mock.patch('tmdbsimple.search.Search',autospec=True)
        stubbedSearchClass = patcher.start()
        stubbedSearch = stubbedSearchClass.return_value
        stubbedSearch.movie.return_value = {'page': 1, 'results': [], 'total_pages': 0, 'total_results': 0} 
        self.addCleanup(patcher.stop)

    def test_thenEmptyResultsArrayReturned(self):
        searchResult = searchByTitle('Pride and Prejudice',1)
        self.assertEqual(searchResult['results'],[])

class WhenApiMovieSearchTermIsEmpty(TestCase):

    def setUp(self):
        patcher = mock.patch('tmdbsimple.search.Search',autospec=True)
        stubbedSearchClass = patcher.start()
        self.stubbedSearch = stubbedSearchClass.return_value
        self.stubbedSearch.movie.side_effect = requests.HTTPError("requests is internal to tmdbsimple and raises an error for empty")
        self.addCleanup(patcher.stop)

    def test_thenEmptyArrayReturned(self):
        try:
          searchResult = searchByTitle('',1)
        except requests.HTTPError as e:
          self.fail()
          return
        self.assertEqual(searchResult,{})

class WhenApiMovieSearchResultPosterPathIsNone(TestCase):

    def setUp(self):
        patcher = mock.patch('tmdbsimple.search.Search',autospec=True)
        stubbedSearchClass = patcher.start()
        self.stubbedSearch = stubbedSearchClass.return_value
        self.stubbedSearch.movie.return_value = {'page': 1, 'results': [
             {'adult': False,
              'backdrop_path': '/2rkwFOAjJY4BFRDa0Ri89L4pScD.jpg',
              'id': 50553,
              'original_title': 'Sherlock Holmes Faces Death',
              'popularity': 0.0419040441936213,
              'poster_path': None,
              'release_date': '1943-09-17',
              'title': 'Sherlock Holmes Faces Death',
              'video': False,
              'vote_average': 5.8,
              'vote_count': 2}], 'total_pages': 0, 'total_results': 0} 
        self.addCleanup(patcher.stop)

    def test_thenDefaultImageUriReturned(self):
        posterDefault = '/static/w92noPoster.jpg'
        searchResult = searchByTitle('zbzbzbz',1)
        self.assertEqual(searchResult['results'][0]['filmImgSrc'],posterDefault)


class WhenApiMovieSearchReturnsResult(TestCase):

    def setUp(self):
        patcher = mock.patch('tmdbsimple.search.Search',autospec=True)
        stubbedSearchClass = patcher.start()
        stubbedSearch = stubbedSearchClass.return_value
        stubbedSearch.movie.return_value = {'page': 1, 'results': [
             {'adult': False,
              'backdrop_path': '/2rkwFOAjJY4BFRDa0Ri89L4pScD.jpg',
              'id': 50553,
              'original_title': 'Sherlock Holmes Faces Death',
              'popularity': 0.0419040441936213,
              'poster_path': '/8ZGyC2xuDDFp1AQ1wtCvK5FGU3w.jpg',
              'release_date': '1943-09-17',
              'title': 'Sherlock Holmes Faces Death',
              'video': False,
              'vote_average': 5.8,
              'vote_count': 2},
             {'adult': False,
              'backdrop_path': '/4MQtUsVSXJOD8MKw4I0MODVuxEd.jpg',
              'id': 169724,
              'original_title': 'Sherlock Holmes nevében',
              'popularity': 0.00200072900013075,
              'poster_path': '/1sxgIbSPoX0NLqGhWO3PYv9oGNV.jpg',
              'release_date': '2012-01-23',
              'title': 'Sherlock Holmes nevében',
              'video': False,
              'vote_average': 0.0,
              'vote_count': 0}
            ], 'total_pages': 0, 'total_results': 0} 
        self.addCleanup(patcher.stop)

    def test_thenFilmTitleIsCorrect(self):
        searchResult = searchByTitle('Sherlock',1)
        self.assertEqual(searchResult['results'][0]['title'],'Sherlock Holmes Faces Death')

    def test_thenImagePathIsCorrect(self):
        searchResult = searchByTitle('Sherlock',1)
        self.assertEqual(searchResult['results'][0]['filmImgSrc'],'https://image.tmdb.org/t/p/w92/8ZGyC2xuDDFp1AQ1wtCvK5FGU3w.jpg')

    def test_thenTheTmdbMovieIdIsCorrect(self):
        searchResult = searchByTitle('Sherlock',1)
        self.assertEqual(searchResult['results'][0]['id'],50553)

    def test_thenSameCountOfResultModelsReturned(self):
        searchResult = searchByTitle('Sherlock',1)
        self.assertEqual(len(searchResult['results']),2)


class WhenGettingSecondPageOfMultiPageResult(TestCase):

    def setUp(self):
        patcher = mock.patch('tmdbsimple.search.Search',autospec=True)
        stubbedSearchClass = patcher.start()
        stubbedSearch = stubbedSearchClass.return_value
        stubbedSearch.movie.return_value = {'page': 2, 'results': [
             {'adult': False,
              'backdrop_path': '/2rkwFOAjJY4BFRDa0Ri89L4pScD.jpg',
              'id': 50553,
              'original_title': 'Sherlock Holmes Faces Death',
              'popularity': 0.0419040441936213,
              'poster_path': '/8ZGyC2xuDDFp1AQ1wtCvK5FGU3w.jpg',
              'release_date': '1943-09-17',
              'title': 'Sherlock Holmes Faces Death',
              'video': False,
              'vote_average': 5.8,
              'vote_count': 2},
             {'adult': False,
              'backdrop_path': '/4MQtUsVSXJOD8MKw4I0MODVuxEd.jpg',
              'id': 169724,
              'original_title': 'Sherlock Holmes nevében',
              'popularity': 0.00200072900013075,
              'poster_path': '/1sxgIbSPoX0NLqGhWO3PYv9oGNV.jpg',
              'release_date': '2012-01-23',
              'title': 'Sherlock Holmes nevében',
              'video': False,
              'vote_average': 0.0,
              'vote_count': 0}
            ], 'total_pages': 2, 'total_results': 4} 
        self.addCleanup(patcher.stop)

    def test_thenFilmTitleIsCorrect(self):
        searchResult = searchByTitle('Sherlock',2)
        self.assertEqual(searchResult['results'][0]['title'],'Sherlock Holmes Faces Death')

    def test_thenImagePathIsCorrect(self):
        searchResult = searchByTitle('Sherlock',2)
        self.assertEqual(searchResult['results'][0]['filmImgSrc'],'https://image.tmdb.org/t/p/w92/8ZGyC2xuDDFp1AQ1wtCvK5FGU3w.jpg')

    def test_thenTheTmdbMovieIdIsCorrect(self):
        searchResult = searchByTitle('Sherlock',2)
        self.assertEqual(searchResult['results'][0]['id'],50553)

    def test_thenSameCountOfResultModelsReturned(self):
        searchResult = searchByTitle('Sherlock',2)
        self.assertEqual(len(searchResult['results']),2)



class WhenGettingNonExistentPageOfMultiPageResult(TestCase):
    #check for exception
    pass
