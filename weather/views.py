from django.shortcuts import render
from .serializers import WeatherSerializer
from .models import Weather
from rest_framework import viewsets


class WeatherDiscription(viewsets.ReadOnlyModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
