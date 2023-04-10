from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    ism = models.CharField(max_length=100)
    rasm = models.FileField(blank=True, null=True)
    tel = models.CharField(max_length=14)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tugilgan_yil = models.DateField()
    jins = models.CharField(max_length=5)
    shahar = models.CharField(max_length=100)
