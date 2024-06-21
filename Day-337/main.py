import pandas as pd
class analyzie_Employee_performance_data:
    def data_summarry(self):
        employee_performance_data = {
            'Employee ID': [1, 2, 3, 4, 5],
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
            'Department': ['Sales', 'Marketing', 'Sales', 'HR', 'Marketing'],
            'Monthly Sales': [5000, 3000, 7000, 2000, 4000],
            'Performance Rating': [4.5, 3.8, 4.9, 3.2, 4.1]
        }

        data = pd.DataFrame(employee_performance_data)

        total_sales = data['Monthly Sales'].sum()
        avrage_performmance_rating = data['Performance Rating'].mean()
        departmment_sales = data.groupby('Department')['Monthly Sales'].sum()
        departmment_avrg_rating = data.groupby('Department')['Performance Rating'].mean()
        top_sales_employee = data.loc[data['Monthly Sales'].idxmax()]['Name']
        top_rating_employee = data.loc[data['Performance Rating'].idxmax()]['Name']

        print(f"Total Sales: {total_sales}\nTotal Department Sales: {departmment_sales}\nAvrage Performance Rating: {avrage_performmance_rating}\nDepartment Avrage Rating: {departmment_avrg_rating}\nTop Rating Employee: {top_rating_employee}\nTop Sales Employee: {top_sales_employee}")

if __name__ == "__main__":
    aepd = analyzie_Employee_performance_data()
    aepd.data_summarry()