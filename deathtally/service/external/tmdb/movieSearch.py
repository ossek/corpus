import tmdbsimple as tmdb
import cgi
from deathtally.apimodels import MovieSearchResult

# todo move these to config
tmdb.API_KEY = "66ce2159c772be3af86f05510178f54f"
BASE_IMAGE_URL = 'https://image.tmdb.org/t/p'

# shows search results.
# single api call
def searchByTitle(searchTerm):
    searcher = tmdb.search.Search()
    result = searcher.movie(query=cgi.escape(searchTerm),search_type="phrase")
    resultModels = []
    resultModels = [makeResultModel(r) for r in result['results']]
    return resultModels

def makeResultModel(tmdbFilmSearchResult):
    resultModel = MovieSearchResult()
    resultModel.filmTitle = tmdbFilmSearchResult['title']
    resultModel.filmImgSrc = '{baseImageUrl}{size}{posterpath}'.format(
            baseImageUrl=BASE_IMAGE_URL,
            size='w96',
            posterpath=tmdbFilmSearchResult['poster_path'])
    return resultModel

# from result of searchForMovieByTitle: result['results'][0]['id']
# single api call
def getCredits(filmId):
 movie = tmdb.movies.Movies(filmId)
 return movie.credits()

def getCastList(filmId):
    return getCredits()['cast']

# shows more data about an individual search result
# single api call
def getFilmAndCastData(filmId):
   movie = tmdb.movies.Movies(filmId)
   return movie.credits()
