from django.db import models
#internal api models
class MovieSearchResult(models.Model):
    filmTitle = ""
    filmImageSrc = ""

    class Meta:
        ordering = ('created',)
