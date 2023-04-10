from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class BolimlarAPIVIew(APIView):
    def get(self, request):
        bolim = Bolim.objects.all()
        serializer = BolimSerializer(bolim, many=True)
        return Response(serializer.data)

class BittaMahsulotAPIView(APIView):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.filter(bolim__id=pk)
        serializer = MahsulotSerializer(mahsulot, many=True)
        return Response(serializer.data)

class ChegirmalarAPIView(APIView):
    def get(self, request):
        chegirma = Mahsulot.objects.order_by("-chegirma")
        serializer = MahsulotSerializer(chegirma, many=True)
        return Response(serializer.data)

class IzohAPIView(APIView):
    def get(self, request, pk):
        izoh = Izoh.objects.filter(mahsulot__id=pk)
        serializer = IzohSerializer(izoh, many=True)
        return Response(serializer.data)