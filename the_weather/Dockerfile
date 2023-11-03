# pull the official base image
FROM python:3.9-alpine
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV WEATHER_API_KEY "3e07ef677a154aab70f09ce2fe9fd3db"
ENV WEATHER_BASE_URL "https://api.openweathermap.org"

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app
EXPOSE 8000