from rest_framework import serializers
from .models import *

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"

class SavatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savat
        fields = "__all__"

class SavatItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavatItem
        fields = "__all__"

class TanlganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanlangan
        fields = "__all__"