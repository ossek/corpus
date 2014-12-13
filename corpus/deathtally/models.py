from django.db import models

class MediaMetaData(models.Model):
    title = models.TextField()
    description = models.TextField()

class TimeInfo(models.Model):
    millisLength = models.IntegerField()

class Film(models.Model):
    timeInfo = models.ForeignKey(TimeInfo)
    mediaMetaData = models.ForeignKey(MediaMetaData)
    wilhelmScreamCount = models.IntegerField()

class Event(models.Model):
    inMedia = models.ForeignKey(MediaMetaData,default=None)
    atTimeMillis = models.IntegerField(default=0)
    name = models.TextField()

class Tag(models.Model):
    on = models.ForeignKey(MediaMetaData,default=None)
    text = models.TextField()

class Person(models.Model):
    realName = models.TextField()

class Character(models.Model):
    inMedia = models.ForeignKey(MediaMetaData)
    person = models.ForeignKey(Person)
    characterName = models.TextField()

class GameInstance(models.Model):
    #associated with a bunch of players
    pass

class Player(models.Model):
    name = models.CharField(max_length=50)
    person = models.ForeignKey(Person)
    ofGame = models.ForeignKey(GameInstance)

class GameSolution(models.Model):
    mediaMetaData = models.ForeignKey(MediaMetaData)

class DeathtallySolution(models.Model):
    ofFilm = models.ForeignKey(Film)


class DeathtallyInstance(models.Model):
    pass

class Death(models.Model):
    inDeathtally = models.ForeignKey(DeathtallySolution)
    who = models.ForeignKey(Character)
    when = models.ForeignKey(Event)



    #place, thing
