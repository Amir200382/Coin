from django.urls import path
from .views import *

urlpatterns = [
    path('price/<str:coin_name>/' , find_price),
]