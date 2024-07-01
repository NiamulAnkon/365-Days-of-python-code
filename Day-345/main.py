import pandas as pd

class Analyzing_Employee_Attendance_Data:
    def data_summarry(self):
        attendance_data = {
            'Employee ID': [1, 2, 3, 1, 2, 3, 1, 2, 3],
            'Date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-03'],
            'Check-In Time': ['09:00', '09:30', '09:15', '09:05', '09:45', '09:00', '09:10', '09:30', '09:20'],
            'Check-Out Time': ['17:00', '17:30', '17:15', '17:05', '17:45', '17:00', '17:10', '17:30', '17:20'],
        }

        df = pd.DataFrame(attendance_data)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Check-In Time'] = pd.to_datetime(df['Check-In Time'], format='%H:%M').dt.time
        df['Check-Out Time'] = pd.to_datetime(df['Check-Out Time'], format='%H:%M').dt.time

        total_check_ins = len(df)
        avg_check_in_time = pd.to_datetime(df['Check-In Time'].astype(str)).dt.time.mean()
        avg_check_out_time = pd.to_datetime(df['Check-Out Time'].astype(str)).dt.time.mean()
        daily_check_ins = df.groupby('Date').size()
        highest_check_ins_day = daily_check_ins.idxmax()

        daily_avg_check_in_time = df.groupby('Date')['Check-In Time'].apply(lambda x: pd.to_datetime(x.astype(str)).dt.time.mean())
        earliest_avg_check_in_day = daily_avg_check_in_time.idxmin()

        daily_avg_check_out_time = df.groupby('Date')['Check-Out Time'].apply(lambda x: pd.to_datetime(x.astype(str)).dt.time.mean())
        latest_avg_check_out_day = daily_avg_check_out_time.idxmax()
        
        df['Check-In Time'] = pd.to_datetime(df['Check-In Time'], format='%H:%M')
        df['Check-Out Time'] = pd.to_datetime(df['Check-Out Time'], format='%H:%M')

        df['Hours Worked'] = (df['Check-Out Time'] - df['Check-In Time']).dt.seconds / 3600

        total_hours_per_employee = df.groupby('Employee ID')['Hours Worked'].sum()
        employee_highest_hours = total_hours_per_employee.idxmax()

        check_in_std_per_employee = df.groupby('Employee ID')['Check-In Time'].apply(lambda x: pd.to_datetime(x.astype(str)).dt.time.std())
        most_consistent_check_in_employee = check_in_std_per_employee.idxmin()

        print(f"Total Number of Check-Ins: {total_check_ins}\nAverage Check-In Time: {avg_check_in_time}\nAverage Check-Out Time: {avg_check_out_time}\nDay with Highest Number of Check-Ins: {highest_check_ins_day}\nDay with Earliest Average Check-In Time: {earliest_avg_check_in_day}\nDay with Latest Average Check-Out Time: {latest_avg_check_out_day}\nTotal Hours Worked per Employee:\n{total_hours_per_employee}\nEmployee with Highest Total Hours Worked: {employee_highest_hours}\nEmployee with Most Consistent Check-In Time: {most_consistent_check_in_employee}")

if __name__ == "__main__":
    aead = Analyzing_Employee_Attendance_Data()
    aead.data_summarry()