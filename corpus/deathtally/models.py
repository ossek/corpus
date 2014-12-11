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
    inMedia = models.ForeignKey(MediaMetaData)
    realName = models.TextField()

class Character(models.Model):
    person = models.ForeignKey(Person)
    characterName = models.TextField()
