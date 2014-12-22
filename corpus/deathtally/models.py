from django.db import models

##essentials:
#game solution
# - list of actor name, death time, image of actor
#    - ie actor name, event, event tag "death", image of actor
# - image of film
# - film name

#possible issues: if tmbd unavailable

#the basic pattern we are following is
#media, event time, tag describing event

class DeathtallySolution(models.Model):
    filmTitle = models.TextField()
    #URI to an image of the film's cover
    filmImageSrc = models.TextField()

class Death(models.Model):
    inDeathtally = models.ForeignKey(DeathtallySolution)
    #todo: distinguishing people with the same name
    actorname = models.TextField()
    when = models.IntegerField(default=0)
    #place, thing
