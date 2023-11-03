from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import WeatherSerializer
from . weatherclient import get_weather
from django.core.cache import cache

@api_view(["GET"])
def getWeatherDetails(request):
    try:
        serializer = WeatherSerializer(data=request.GET)
        serializer.is_valid()
        city = serializer.validated_data['city']
    except:
        return Response({"message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    #  Low level cache API
    if cache_data := cache.get("{}".format(city)):
        return Response(cache_data)
    weather_data = get_weather(city)
    cache.set("{}".format(city),weather_data, timeout=60*3)
    return Response(weather_data)
