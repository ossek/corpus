import tmdbsimple as tmdb
import cgi
from deathtally.apimodels import MovieSearchResult
from . tmdbImageUrls import makeFilmImgUri
from . import configuration

# from result of searchForMovieByTitle: result['results'][0]['id']
# single api call
def getCast(filmId):
    movie = tmdb.movies.Movies(filmId)
    cast = movie.credits()['cast']
    size = "w92"
    for castMember in cast:
        castMember['filmImgSrc'] = makeFilmImgUri(configuration.BASE_IMAGE_URL,
                size,
                castMember['profile_path'])
    return cast

def getMovieInfo(filmId):
    movie = tmdb.movies.Movies(filmId)
    return movie.info()
