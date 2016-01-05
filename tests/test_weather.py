import pytest

from utils.open_weathermap_api_calls import OpenweathermapAPICalls
from resources import config
from utils.converter import Converter


class TestWeather(object):
    @classmethod
    def setup_class(cls):
        cls.weather_api = OpenweathermapAPICalls()

    @pytest.mark.parametrize('city', [config.Kyiv, config.Boston, config.London])
    def test_get_imp_weather_by_id(self, city):
        """Compare weather parameters with imperial unit
         get by city ID and city Name"""
        response_by_name = self.weather_api.get_imperial_weather_by_name(city)
        assert response_by_name.status_code == 200

        response_by_id = self.weather_api.get_imperial_weather_by_id(city)
        assert response_by_id.status_code == 200

        weather_by_id = response_by_id.json()
        weather_by_name = response_by_name.json()

        for key in weather_by_name:
            assert weather_by_name[key] == weather_by_id[key]

    @pytest.mark.parametrize('city', [config.Kyiv, config.Boston, config.London])
    def test_get_imp_weather_by_geo_loc(self, city):
        """Compare weather parameters with imperial unit
         get by city geographic location and city Name"""
        response_by_name = self.weather_api.get_imperial_weather_by_name(city)
        assert response_by_name.status_code == 200

        response_by_geo_loc = self.weather_api.get_imperial_weather_by_geo_location(city)
        assert response_by_geo_loc.status_code == 200

        weather_by_geo_loc = response_by_geo_loc.json()
        weather_by_name = response_by_name.json()

        keys = {'coord', 'weather', 'main'}
        for key in keys:
            assert weather_by_name[key] == weather_by_geo_loc[key]

    @pytest.mark.parametrize('city', [config.Kyiv, config.Boston, config.London])
    def test_weather_metrics(self, city):
        """Compere temperature parameters of metrics and imperial units"""
        imperial_weather = self.weather_api.get_imperial_weather_by_name(city)
        assert imperial_weather.status_code == 200

        metric_weather = self.weather_api.get_metric_weather_by_name(city)
        assert metric_weather.status_code == 200

        cels_temp = metric_weather.json()['main']['temp']
        fahr_temp = imperial_weather.json()['main']['temp']

        converted_temp = Converter.fahrenheit_to_celsius(fahr_temp)

        assert cels_temp == converted_temp

        cels_temp_min = metric_weather.json()['main']['temp_min']
        fahr_temp_min = imperial_weather.json()['main']['temp_min']

        converted_temp_min = Converter.celsius_to_fahrenheit(cels_temp_min)

        assert fahr_temp_min == converted_temp_min

        cels_temp_max = metric_weather.json()['main']['temp_max']
        fahr_temp_max = imperial_weather.json()['main']['temp_max']

        converted_temp_max = Converter.fahrenheit_to_celsius(fahr_temp_max)

        assert cels_temp_max == converted_temp_max

    @pytest.mark.parametrize('city', [config.Kyiv, config.Boston, config.London])
    def test_get_metr_weather_by_id(self, city):
        """Compare weather parameters with metrics unit
         get by city ID and city Name"""
        response_by_name = self.weather_api.get_metric_weather_by_name(city)
        assert response_by_name.status_code == 200

        response_by_id = self.weather_api.get_metric_weather_by_id(city)
        assert response_by_id.status_code == 200

        weather_by_id = response_by_id.json()
        weather_by_name = response_by_name.json()

        for key in weather_by_name:
            assert weather_by_name[key] == weather_by_id[key]

    @pytest.mark.parametrize('city', [config.Kyiv, config.Boston, config.London])
    def test_get_metr_weather_by_geo_loc(self, city):
        """Compare weather parameters with metrics unit
         get by city geographic location and city Name"""
        response_by_name = self.weather_api.get_metric_weather_by_name(city)
        assert response_by_name.status_code == 200

        response_by_geo_loc = self.weather_api.get_metric_weather_by_geo_location(city)
        assert response_by_geo_loc.status_code == 200

        weather_by_geo_loc = response_by_geo_loc.json()
        weather_by_name = response_by_name.json()

        keys = {'coord', 'weather', 'main'}
        for key in keys:
            assert weather_by_name[key] == weather_by_geo_loc[key]
