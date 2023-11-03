from django.urls import path
from weather import views

urlpatterns = [
    path(
        route = 'weather',
        view = views.getWeatherDetails,
    )
]
