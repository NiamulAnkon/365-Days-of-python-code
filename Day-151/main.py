import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")
        self.master.geometry("600x400")

        # Set the background color to gray
        self.master.configure(bg="#C0C0C0")

        # Create GUI elements with larger font size
        label_font = ("Arial", 20)
        button_font = ("Arial", 14)

        self.city_label = tk.Label(self.master, text="Enter City:", font=label_font, bg="#C0C0C0")
        self.city_label.pack(pady=20)
        
        self.city_entry = tk.Entry(self.master, font=label_font)
        self.city_entry.pack(pady=10)

        self.get_weather_button = tk.Button(self.master, text="Get Weather", command=self.get_weather, font=button_font, bg="Black",fg="White")
        self.get_weather_button.pack(pady=20)

        self.weather_result_label = tk.Label(self.master, text="", font=label_font, bg="#C0C0C0")
        self.weather_result_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            try:
                # Use a weather API (replace 'YOUR_API_KEY' with your actual API key)
                api_key = '95aea3dfcd260719b61b3c8c1100e75a'
                url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
                response = requests.get(url)
                data = response.json()

                # Extract relevant weather information
                temperature_kelvin = data['main']['temp']
                temperature_celsius = temperature_kelvin - 273.15
                humidity = data['main']['humidity']
                weather_description = data['weather'][0]['description']

                result_text = f'Temperature: {temperature_celsius:.2f} °C\nHumidity: {humidity}%\nCondition: {weather_description}'
                self.weather_result_label.config(text=result_text)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a city.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
