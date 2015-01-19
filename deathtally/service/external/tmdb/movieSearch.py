import tmdbsimple as tmdb
import cgi
from deathtally.apimodels import MovieSearchResult
from . tmdbImageUrls import makeFilmImgUri
from . import configuration

tmdb.API_KEY = configuration.TMDB_API_KEY
BASE_IMAGE_URL = configuration.BASE_IMAGE_URL

# shows search results.
# single api call
def searchByTitle(searchTerm):
    strippedSearchTerm = searchTerm.strip()
    resultModels = []
    if(strippedSearchTerm == ''):
        return resultModels
    searcher = tmdb.search.Search()
    result = searcher.movie(query=cgi.escape(searchTerm),search_type="phrase")
    if(len(result) > 0 and 'results' in result):
        resultModels = [makeResultModel(r) for r in result['results']]
    return resultModels

def makeResultModel(tmdbFilmSearchResult):
    resultModel = MovieSearchResult()
    resultModel.filmTitle = tmdbFilmSearchResult['title']
    #todo make image size a config setting
    size = "w92"
    if tmdbFilmSearchResult['poster_path']:
        resultModel.filmImgSrc = makeFilmImgUri(BASE_IMAGE_URL,size,tmdbFilmSearchResult['poster_path'])
    else:
        resultModel.filmImgSrc = makeFilmImgUri('/static',size,'noPoster.jpg')
    resultModel.tmdbMovieId = tmdbFilmSearchResult['id']
    return resultModel

# shows more data about an individual search result
# single api call
def getFilmAndCastData(filmId):
   movie = tmdb.movies.Movies(filmId)
   return movie.credits()
