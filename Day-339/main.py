import pandas as pd

class fitnes_tracker_data_analyzie:
    def data_summary(self):
        fitness_data = {
            'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Steps': [8000, 9500, 7000, 10000, 8500],
            'Calories Burned': [300, 350, 280, 400, 320],
            'Active Minutes': [45, 60, 30, 70, 50],
            'Sleep Hours': [7.5, 8.0, 6.5, 8.0, 7.0]
        }
        
        data = pd.DataFrame(fitness_data)

        total_steps = data['Steps'].sum()
        avrg_calories_burned = data['Calories Burned'].mean()
        avrg_actv_minutes = data['Active Minutes'].mean()
        avrg_slp_hrs = data['Sleep Hours'].mean()

        print(f"total steps taken over the period: {total_steps}\naverage calories burned per day: {avrg_calories_burned}\naverage active minutes per day: {avrg_actv_minutes}\naverage sleep hours per day: {avrg_slp_hrs}")

if __name__ == "__main__":
    ftda = fitnes_tracker_data_analyzie()
    ftda.data_summary()