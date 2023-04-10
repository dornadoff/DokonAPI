from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class BolimlarAPIVIew(APIView):
    def get(self, request):
        bolim = Bolim.objects.all()
        serializer = BolimSerializer(bolim)
        return Response(serializer.data)
