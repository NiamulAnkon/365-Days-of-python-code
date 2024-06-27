import pandas as pd

class Analyzing_Weather_Data:
    def data_summarry(self):
        data = {
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07'],
            'Temperature (°C)': [5, 6, 7, 8, 10, 12, 9],
            'Humidity (%)': [85, 80, 78, 75, 70, 65, 72],
            'Precipitation (mm)': [2.0, 0.0, 1.0, 0.5, 0.0, 0.0, 0.0]
        }

        df = pd.DataFrame(data)

        avg_temperature = df['Temperature (°C)'].mean()
        total_precipitation = df['Precipitation (mm)'].sum()
        avg_humidity = df['Humidity (%)'].mean()
        highest_temperature_day = df.loc[df['Temperature (°C)'].idxmax()]['Date']
        highest_humidity_day = df.loc[df['Humidity (%)'].idxmax()]['Date']
        highest_precipitation_day = df.loc[df['Precipitation (mm)'].idxmax()]['Date']

        
        print(f"Avrage Temperature: {avg_temperature}\nTotal Preciption: {total_precipitation}\nAvrage Humidity: {avg_humidity}\nHighest Temperature Day: {highest_temperature_day}\nHighest Humidity Day: {highest_humidity_day}\n Highest Preciption Day: {highest_precipitation_day}")

if __name__ == "main":
    awd = Analyzing_Weather_Data
    awd.data_summarry()