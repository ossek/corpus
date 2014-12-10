from django.db import models

class Media(models.Model):
    title = models.TextField()
    description = models.TextField()

class TimeMedia(Media):
    minutesLength = models.IntegerField()

class Film(TimeMedia):
    wilhelmScreamCount = models.IntegerField()

class Song(TimeMedia):
    pass

class Event(models.Model):
    inFilm = models.ForeignKey(TimeMedia,default=None)
    name = models.TextField()

class Tag(models.Model):
    on = models.ForeignKey(Media,default=None)
    text = models.TextField()
