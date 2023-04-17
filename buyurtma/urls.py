from django.urls import path, include
from .views import *

urlpatterns = [
    path("", BuyurtmaAPIView.as_view()),
    path("savat/item/", SavatItemAPIView.as_view())
]