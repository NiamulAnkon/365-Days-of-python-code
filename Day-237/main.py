#Excirse
import pandas as pd

#What was the average temperature in first week of Jan
df = pd.read_csv('nyc_weather.csv')

df['date'] = pd.to_datetime(df['date'], format='%b %d')

first_week_jan = df[(df['date'].dt.month == 1) & (df['date'].dt.day_of_week == 1)]

average_temp = first_week_jan['temperature(F)'].mean()

print(f"Average temperature in the first week of January: {average_temp}")

#What was the maximum temperature in first 10 days of Jan
jan_data = df[df['date'].dt.month == 1]

jan_date_sort = jan_data.sort_values(by='date')

f_10_dats_jan = jan_date_sort.head(10)

max_temp_f_10_days_jan = f_10_dats_jan['temperature(F)'].max()

print(f"Max Temp in jan is: {max_temp_f_10_days_jan}")

#What was the temperature on Jan 9?
jan_9_data = df[df['date'].dt.day == 9]

if not jan_9_data.empty:
    temp_9_jan = jan_9_data.iloc[0]['temperature(F)']
    print(f"Temperature on January 9th:{temp_9_jan}")
else:
    print("No data is avilable")

#What was the temperature on Jan 4?
jan_4_data = df[df['date'].dt.day == 4]

if not jan_4_data.empty:
    temp_jan_4 = jan_4_data.iloc[0]['temperature(F)']
    print(f"Temperature on January 4th {temp_jan_4}")
else:
    print("No data avilable")