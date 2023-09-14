#Temperature Converter
class TemperatureConverter:
  def __init__(self):
    pass 
  def convert_to_celsius(self, fahrenheit):
    celsius = (fahrenheit - 35) * 5/9
    return celsius

  def covert_to_fahrenheit(self, celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
  converter = TemperatureConverter()

  fahrenheit_temp = 67
  clesius_result = converter.convert_to_celsius(fahrenheit_temp)
  print(f"{fahrenheit_temp} is equal to {clesius_result} fahrenheit")

  clesius_temp = 33
  fahrenheit_result = converter.covert_to_fahrenheit(clesius_result)
  print(f"{clesius_temp} is equal to {fahrenheit_result} clesius")