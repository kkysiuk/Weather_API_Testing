import requests

from utils import open_weathermap_config as config


class OpenweathermapAPICalls(object):

    def get_metric_weather_by_id(self, city):
        """Get weather in metric units by city ID"""
        r = requests.get(config.METRIC_WEATHER_BY_CITY_ID % city['id'])
        return r

    def get_metric_weather_by_name(self, city):
        """Get weather in metric units by city Name"""
        r = requests.get(config.METRIC_WEATHER_BY_CITY_NAME% city['name'])
        return r

    def get_metric_weather_by_geo_location(self, city):
        """Get weather in metric units by city geographic location"""
        lon = city['geographic coordinates']['lon']
        lat = city['geographic coordinates']['lat']

        r = requests.get(config.METRIC_WEATHER_BY_CITY_GEO_LOCATION % (lat, lon))
        return r

    def get_imperial_weather_by_id(self, city):
        """Get weather in imperial units by city ID"""
        r = requests.get(config.IMPERIAL_WEATHER_BY_CITY_ID% city['id'])
        return r

    def get_imperial_weather_by_name(self, city):
        """Get weather in imperial units by city Name"""
        r = requests.get(config.IMPERIAL_WEATHER_BY_CITY_NAME% city['name'])
        return r

    def get_imperial_weather_by_geo_location(self, city):
        """Get weather in imperial units by city geographic location"""
        lon = city['geographic coordinates']['lon']
        lat = city['geographic coordinates']['lat']

        r = requests.get(config.IMPERIAL_WEATHER_BY_CITY_GEO_LOCATION % (str(lat), str(lon)))
        return r
