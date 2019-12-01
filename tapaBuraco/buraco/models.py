from django.db import models

# Create your models here.

class Usuario(models.Model):
	email = models.EmailField()
	senha = models.CharField(max_length=15)
	def __str__(self):
		return self.email

class Cidadao(models.Model):
	userid = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	holesDetected = models.IntegerField(blank=True, null=True)
	totalAvgAcc = models.FloatField(blank=True, null=True)

class Buraco(models.Model):
	latitude = models.DecimalField(max_digits=20, decimal_places=7)
	longitude = models.DecimalField(max_digits=20, decimal_places=7)
	acc =  models.FloatField()
	cidadao = models.ManyToManyField(Cidadao,blank=True, null=True)
	situacao = models.CharField(max_length=50, default="Não resolvido")
	data_adicao = models.DateTimeField(auto_now=True)

class Agente(models.Model):
	userid = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	lastKnownLat = models.DecimalField(max_digits=20, decimal_places=7)
	lastKnownLon = models.DecimalField(max_digits=20, decimal_places=7)