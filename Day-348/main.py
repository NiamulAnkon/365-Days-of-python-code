import pandas as pd

class Employee_Performance_Analysis:
    def analyzie(self):
        employee_performance_data = {
            'Employee ID': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008', 'E009', 'E010'],
            'Name': ['John Smith','Jane Doe','Bob Brown','Alice Green','Mike White','Emma Black','Sam Blue','Lisa Yellow','Tom Orange','Sarah Pink'],
            'Department': ['Sales', 'Marketing', 'Sales', 'IT', 'Marketing', 'IT', 'Sales', 'Marketing', 'IT', 'Sales'],
            'Performance Score': [85, 90, 78, 95, 88, 92, 80, 85, 89, 82],
        }

        df = pd.DataFrame(employee_performance_data)

        total_employee = df['Employee ID'].count()
        avrage_performance_score = df['Performance Score'].mean()
        top_3_emplyees_by_performance_score = df.nlargest(3, 'Performance Score')['Name']
        performance_score_by_department = df.groupby('Department')['Performance Score'].mean()

        print(f"Total Employes: {total_employee}\nAvrage Performance Score: {avrage_performance_score}\nTop 3 Employees By Performance:\n{top_3_emplyees_by_performance_score}\nAvrage Performance Score By Department: {performance_score_by_department}")


if __name__ == "__main__":
    epa = Employee_Performance_Analysis()
    epa.analyzie()