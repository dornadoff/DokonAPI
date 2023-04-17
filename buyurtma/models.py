from django.db import models
from django.db.models import Sum
from userapp.models import *
from asosiy.models import *

class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True, null=True)

class SavatItem(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    yetkazish_kuni = models.PositiveSmallIntegerField(default=4)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE, related_name="itemlari")
    umumiy_summa = models.IntegerField(blank=True, null=True)
    yetkazish_puli = models.PositiveSmallIntegerField(default=15000)

    def save(self, *args, **kwargs):
        narx = self.mahsulot.narx-(self.mahsulot.narx*self.mahsulot.chegirma/100)
        self.umumiy_summa = self.miqdor * narx + self.yetkazish_puli
        super().save(*args, **kwargs)

class Buyurtma(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    holat = models.CharField(max_length=30)
    sana = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        itemlar = self.savat.itemlari.all()
        itemlar.aggregate(summasi=Sum("umumiy_summa"))
        super().save(*args, **kwargs)
