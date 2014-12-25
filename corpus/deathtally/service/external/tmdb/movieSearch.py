import tmdbsimple as tmdb
import cgi

tmdb.API_KEY = "66ce2159c772be3af86f05510178f54f"

# shows search results.
# single api call
def searchForTitles(searchTerm):
    searcher = tmdb.search.Search()
    result = searcher.movie(query=cgi.escape(titlequery),search_type="phrase")
    pass

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
