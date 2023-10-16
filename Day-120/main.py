import requests
import json

# Your OpenWeatherMap API key
API_KEY = "95aea3dfcd260719b61b3c8c1100e75a"

# Function to get the weather data for a location
def get_weather_data(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # You can change units to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        return data
    else:
        return None

# Function to display the weather data
def display_weather_data(weather_data):
    print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Description: {weather_data['weather'][0]['description']}")
    print(f"Pressure: {weather_data['main']['pressure']} hPa")
    print(f"Humidity: {weather_data['main']['humidity']}%")

# Function to get the 3-day weather forecast
def get_weather_forecast(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # You can change units to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == "200":
        return data["list"][:8]  # Extract the next 8 forecast entries (3 days)
    else:
        return None

# Function to display the 3-day weather forecast
def display_weather_forecast(forecast_data):
    print("3-Day Weather Forecast:")
    for entry in forecast_data:
        date_time = entry["dt_txt"]
        temperature = entry["main"]["temp"]
        description = entry["weather"][0]["description"]
        print(f"{date_time}: {temperature}°C, {description}")

# Main function
def main():
    city_name = input("Enter the name of the city or location: ")

    weather_data = get_weather_data(city_name)
    if weather_data:
        display_weather_data(weather_data)
    else:
        print("Weather data not found for the specified location.")

    forecast_data = get_weather_forecast(city_name)
    if forecast_data:
        display_weather_forecast(forecast_data)
    else:
        print("Weather forecast not available for the specified location.")

if __name__ == "__main__":
    main()
