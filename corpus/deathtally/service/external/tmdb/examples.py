import tmdbsimple as tmdb
import cgi

#todo make a cmd line arg or lock it down somehow
tmdb.API_KEY = "<API KEY HERE>"

#the return type is like
#{'page' : 1,
#        'results' :....
#where a given result is like:
#{'adult': False,
# 'backdrop_path': '/vsJZ4VevCDbUW2GESRr3rDNrZlZ.jpg',
# 'id': 164721,
# 'original_title': 'Pride and Prejudice',
# 'popularity': 0.0311596697595292,
# 'poster_path': '/AukVKsjZOVR2CBfI3vSJRXNLEKr.jpg',
# 'release_date': '1995-09-24',
# 'title': 'Pride and Prejudice',
# 'vote_average': 7.1,
# 'vote_count': 24}
def searchForMovieByTitle(titlequery):
    searcher = tmdb.search.Search()
    result = searcher.movie(query=cgi.escape(titlequery),search_type="phrase")
    return result

#from result of searchForMovieByTitle: result['results'][0]['id']
def getCredits(filmId):
    movie = tmdb.movies.Movies(filmId)
    return movie.credits()

def getCastList(filmId):
    return getCredits()['cast']

def getCrewList(filmId):
    return getCredits()['crew']

#the content property on the returned object is the raw image data
#in practice, could probably just use the url as img src in a page
def getMoviePoster(posterpath):
    configinfo = getConfigInfo()
    firstsize = configinfo['images']['poster_sizes'][0]
    baseurl = configinfo['images']['base_url']
    url = '{base}/{size}/{path}'.format(base=baseurl,size=firstsize,path=posterpath)
    return requests.get(url)

def main():
    result = searchForMovieByTitle('anaconda 3')
    print(result)

if __name__ == "__main__":
    main()
