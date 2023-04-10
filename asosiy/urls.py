from django.urls import path
from .views import *

urlpatterns = [
    path('', BolimlarAPIVIew.as_view()),
    path('<int:pk>/mahsulotlar/', BolimMahsulotAPIView.as_view()),
    path('mahsulot/<int:pk>/izohlar/', IzohAPIView.as_view()),
    path("chegirmalar/", ChegirmalarAPIView.as_view())
]
