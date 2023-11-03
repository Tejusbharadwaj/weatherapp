
import os
from urllib.parse import urlencode, urljoin, quote_plus

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = os.environ.get("WEATHER_BASE_URL", 'https://api.openweathermap.org')

def buildUrl(path, format):
     format["appid"]=API_KEY
     query = "?" + urlencode(format, quote_via=quote_plus)
     return urljoin(BASE_URL, path + query)
