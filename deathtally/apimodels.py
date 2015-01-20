#from django.db import models
#internal api models
class MovieSearchResult(object):

    def __init__(self):
        self.filmTitle = ""
        self.filmImgSrc = ""
        self.tmdbMovieId = ""

class MovieCredentialsDict(object):

    def __init__(self):
        pass
        #self.castId = 0
        #self.character = ""
        #self.creditId = 0
        #self.id = 0
        #self.name = ""
        #self.order = -1 
        #self.personImgSrc = ""
