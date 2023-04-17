from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from userapp.models import *


class BuyurtmaAPIView(APIView):
    def get(self, request):
        buyurtma = Buyurtma.objects.filter(profil__user=request.user)
        serializer = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=Profil.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors)

class SavatItemAPIView(APIView):
    def get(self, request):
        savat_item = SavatItem.objects.filter(savat__profil__user=request.user  )
        serializer = SavatItemSerializer(savat_item, many=True)
        return Response(serializer.data)
