
class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp
class CelsiusToFahrenheit (TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32
class CelsiusToKelvin (TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15
class FahrenheitToCelcius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32)*9/5
class KelvinToCelcius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 273.15)


tempInCelsius = float(input("Enter the temperature in Celsius: "))
CelsiusToKelvin = CelsiusToKelvin(tempInCelsius)
print(str(CelsiusToKelvin.conversion()) + " Kelvin")
CelsiusToFahrenheit = CelsiusToFahrenheit(tempInCelsius)
print(str(CelsiusToFahrenheit.conversion()) + " Fahrenheit")
FahrenheitToCelcius= FahrenheitToCelcius(tempInCelsius)
print(str(FahrenheitToCelcius.conversion()) + " Celsius")
KelvinToCelcius =  KelvinToCelcius(tempInCelsius)
print(str(KelvinToCelcius.conversion()) + " Celsius")