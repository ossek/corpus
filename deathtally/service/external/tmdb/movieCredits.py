import tmdbsimple as tmdb
import cgi
from deathtally.apimodels import MovieSearchResult

# todo move these to config
tmdb.API_KEY = "66ce2159c772be3af86f05510178f54f"
BASE_IMAGE_URL = 'https://image.tmdb.org/t/p'

# from result of searchForMovieByTitle: result['results'][0]['id']
# single api call
def getCast(filmId):
 movie = tmdb.movies.Movies(filmId)
 cast = movie.credits()['cast']

