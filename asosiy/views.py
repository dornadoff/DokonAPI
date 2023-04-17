from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

class BolimlarAPIVIew(APIView):
    def get(self, request):
        bolim = Bolim.objects.all()
        serializer = BolimSerializer(bolim, many=True)
        return Response(serializer.data)

class BolimMahsulotAPIView(APIView):
    def get(self, request, pk):
        nom = request.query_params.get("qidirish")
        if nom is None:
            mahsulot = Mahsulot.objects.filter(bolim__id=pk)
        else:
            mahsulot = Mahsulot.objects.filter(bolim__id=pk, nom__contains=nom)
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

    def post(self, request, pk):
        serializer = IzohSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MahsulotAPIView(APIView):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        serializer = MahsulotSerializer(mahsulot)
        return Response(serializer.data)

