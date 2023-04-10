from django.db import models
from userapp.models import *

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rams = models.FileField(null=True, blank=True)

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.FloatField()
    chegirma = models.IntegerField()
    brend = models.CharField(max_length=100)
    batafsil = models.CharField(max_length=500)
    rasm = models.FileField(blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, null=True)
    holat = models.CharField(max_length=100, null=True)
    sotuvchi = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True)

class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    matn = models.CharField(max_length=500)
    reyting = models.FloatField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    sana = models.DateField()
