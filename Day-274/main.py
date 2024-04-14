import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Weather App')
        self.setGeometry(100, 100, 400, 400)

        self.city_label = QLabel('Enter City Name:')
        self.city_input = QLineEdit()
        self.fetch_button = QPushButton('Fetch Weather')
        self.weather_label = QLabel()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.city_label)
        self.layout.addWidget(self.city_input)
        self.layout.addWidget(self.fetch_button)
        self.layout.addWidget(self.weather_label)

        self.fetch_button.clicked.connect(self.fetch_weather)

        self.setLayout(self.layout)

    def fetch_weather(self):
        city = self.city_input.text()
        if not city:
            QMessageBox.warning(self, 'Warning', 'Please enter a city name.')
            return

        api_key = '95aea3dfcd260719b61b3c8c1100e75a'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_desc = data['weather'][0]['description'].capitalize()
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                weather_info = f'Weather: {weather_desc}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'
                self.weather_label.setText(weather_info)
            else:
                QMessageBox.warning(self, 'Error', 'Failed to fetch weather data. Please try again later.')

        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Error', 'An unexpected error occurred. Please try again later.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
