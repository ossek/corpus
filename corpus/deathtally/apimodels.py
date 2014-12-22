#internal api models
class MovieSearchResult():
    filmTitle = ""
    filmImageSrc = ""
    class Meta:
        ordering = ('created',)
