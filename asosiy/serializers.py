from rest_framework import serializers
from .models import *
from django.db.models import Avg

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields = "__all__"

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"

    def validate_chegirma(self, chegirma):
        if chegirma < 0 or chegirma > 50:
            raise serializers.ValidationError("Chegirma 0 dan kichik yoki 50 dan baland foizda bo'lishi mumkin emas")
        return chegirma

    def to_representation(self, instance):
        malumot = super().to_representation(instance)
        malumot["yangi_narx"] = instance.narx - (instance.chegirma * instance.narx // 100)
        izohlar = Izoh.objects.filter(mahsulot=instance)
        malumot["ortacha_reyting"] = izohlar.aggregate(avg_marks=Avg('reyting'))['avg_marks']

        return malumot

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = "__all__"

    def validate_reyting(self, izoh):
        if izoh > 5 or izoh < 0:
            raise serializers.ValidationError("Noto'g'ri reyting bal kiritildi!")
        return izoh
