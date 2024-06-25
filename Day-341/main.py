import pandas as pd

class Analyzing_Restaurant_Sales_Data:
    def data_summarry(self):
        sales_data = {
            'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-04', '2024-01-04'],
            'Item': ['Burger', 'Fries', 'Burger', 'Fries', 'Salad', 'Burger', 'Fries', 'Salad'],
            'Quantity Sold': [50, 100, 60, 80, 40, 70, 90, 50],
            'Price per Item': [5, 2, 5, 2, 4, 5, 2, 4],
            'Total Revenue': [250, 200, 300, 160, 160, 350, 180, 200]
        }
        data = pd.DataFrame(sales_data)

        total_revenue = data['Total Revenue'].sum()
        total_sold = data['Quantity Sold'].sum()
        total_quntity_sold_each_item = data.groupby('Item')['Quantity Sold'].sum()
        total_revuene_each_item = data.groupby('Item')['Total Revenue'].sum()
        data['Date'] = pd.to_datetime(data['Date'])
        daily_total_revenue = data.groupby('Date')['Total Revenue'].sum()
        daily_total_quantity = data.groupby('Date')['Quantity Sold'].sum()
        highest_revenue_day = daily_total_revenue.idxmax()
        highest_quantity_day = daily_total_quantity.idxmax()
        print(f"Total Reveeune: {total_revenue}\nTotal Sold: {total_sold}\nTotal Quantity Sold Each Item: {total_quntity_sold_each_item}\nTotal Revune of Each Item: {total_revuene_each_item}\nHighest Revuneue Day: {highest_revenue_day}\nHighest Quantity Day: {highest_quantity_day}")


if __name__ == "__main__":
    arsd = Analyzing_Restaurant_Sales_Data()
    arsd.data_summarry()
