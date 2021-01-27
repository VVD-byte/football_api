from django.db import models


class Comands(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=200)


class Sorev(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=200)


class Game(models.Model):
    comands1 = models.ForeignKey(Comands)
    comands2 = models.ForeignKey(Comands)
    goal1 = models.IntegerField()
    goal2 = models.IntegerField()
    date = models.DateTimeField()
    sorev = models.ForeignKey(Sorev)
