from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status

from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

class ProfilCreateAPI(APIView):
    def post(self, request):
        serializer = ProfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BittaProfilAPIView(APIView):
    def get(self, request, pk):
        profil = Profil.objects.get(id=pk)
        serializer = ProfilSerializer(profil)
        return Response(serializer.data)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data["username"])
            user = authenticate(username=serializer.data['username'],
                                password=serializer.data['password'])

            if user is None:
                return Response({"xabar": "Username yoki pasword notog'ri"}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({"xabar": "Tizimga kirildi"})
        return Response(serializer.errors)
