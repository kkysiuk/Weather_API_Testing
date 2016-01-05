

class Converter(object):

    @staticmethod
    def fahrenheit_to_celsius(t_fahrenheit):
        """Conversion from Fahrenheit to Celsius"""
        t_celsius = (float(t_fahrenheit) - 32) / 1.8
        return round(t_celsius, 2)

    @staticmethod
    def celsius_to_fahrenheit(t_celsius):
        """Conversion from Celsius to Fahrenheit"""
        t_fahrenheit = (float(t_celsius) * 1.8) + 32
        return round(t_fahrenheit, 2)
