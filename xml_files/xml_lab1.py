import xml.etree.ElementTree as ET

class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.0/5.0 * temperature_in_celsius + 32


class ForecastXmlParser:
    def __init__(self, temperature_converter):
        self.temperature_converter = temperature_converter

    def parse(self, file):
        tree = ET.parse(file)
        root = tree.getroot()

        for child in root:
            week_day = child.find("day").text

            celsius = int(child.find("temperature_in_celsius").text)
            
            fahrenheit = self.temperature_converter.convert_celsius_to_fahrenheit(celsius)
            fahrenheit = round(fahrenheit, 1)
            
            print("{0}: {1} Celsius, {2} Fahrenheit".format(
                week_day, celsius, fahrenheit)
            )

temperature_converter = TemperatureConverter()
forecast_xml_parser = ForecastXmlParser(temperature_converter)
forecast_xml_parser.parse("forecast.xml")