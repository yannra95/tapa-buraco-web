from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=50)
	holesDetected = models.IntegerField(blank=True, null=True)
	totalAvgAcc = models.FloatField(blank=True, null=True)

class Buraco(models.Model):
	latitude = models.CharField(max_length=20)
	longitude = models.CharField(max_length=20)
	acc =  models.FloatField()
	user = models.ManyToManyField(User,blank=True, null=True)

class Agent(models.Model):
	name = models.CharField(max_length=50)
	lastKnownLat = models.CharField(max_length=20)
	lastKnownLon = models.CharField(max_length=20)