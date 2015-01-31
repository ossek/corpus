import tmdbsimple as tmdb
import cgi
from deathtally.apimodels import MovieSearchResult
from . tmdbImageUrls import makeFilmImgUri
from . import configuration

tmdb.API_KEY = configuration.TMDB_API_KEY
BASE_IMAGE_URL = configuration.BASE_IMAGE_URL

# shows search results.
# single api call
def searchByTitle(searchTerm,pageNum):
    strippedSearchTerm = searchTerm.strip()
    resultModels = {}
    if(strippedSearchTerm == ''):
        return resultModels
    searcher = tmdb.search.Search()
    resultModel = searcher.movie(query=cgi.escape(searchTerm),search_type="phrase",page=pageNum)
    for result in resultModel['results']:
        setFilmImgSrc(result)
    return resultModel

def setFilmImgSrc(result):
    #todo make image size a config setting
    size = "w154"
    if result['poster_path']:
        result['filmImgSrc'] = makeFilmImgUri(BASE_IMAGE_URL,size,result['poster_path'])
    else:
        result['filmImgSrc'] = makeFilmImgUri('/static',size,'noPoster.jpg')
