from django.urls import path, include
from .views import *

urlpatterns = [
    path("profil/create/", ProfilCreateAPI.as_view()),
    path("<int:pk>/", BittaProfilAPIView.as_view()),
    path("login/", LoginAPIView.as_view())
]