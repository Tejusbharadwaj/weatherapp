""" Open weather map request handler """

import requests
import json

from django.core import serializers


from . utils  import buildUrl

def _getLatLong(city):
    url = buildUrl("geo/1.0/direct", {"q": city, "limit":5})
    resp = requests.get(url)
    data = resp.json()
    loc = {
        'lat': data[0].get("lat"),
        'lon': data[0].get("lon")
    }
    return loc

def get_weather(city):
    inData = _getLatLong(city)
    inData['units']='metric'
    url = buildUrl("data/2.5/weather", inData)
    resp = requests.get(url)
    data = resp.json()

    localtion_name = "{}".format(data['name'])
    resp_obj = {
        "city": localtion_name,
        "temp": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "temp_max": data['main']['temp_max'],
        "temp_min": data['main']['temp_min'],
        "humidity": data['main']['humidity'],
        "sunrise": data['sys']['sunrise'],
        "sunset": data['sys']['sunset'],
    }
    return resp_obj
