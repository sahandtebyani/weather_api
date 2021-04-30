from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = (
            'id', 'weather_description', 'temperature', 'created_on'
        )