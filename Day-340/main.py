import pandas as pd

class Analyzing_Ecommerce_Order_Data:
    def data_summary(slef):
        order_data = {
            'Order ID': [1, 2, 3, 4, 5],
            'Customer ID': [101, 102, 103, 104, 101],
            'Order Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
            'Quantity': [2, 1, 3, 1, 2],
            'Price per Unit': [25, 45, 25, 35, 45],
            'Total Price': [50, 45, 75, 35, 90],
        }

        data = pd.DataFrame(order_data)

        total_revune = data['Total Price'].sum()
        total_numbers_of_orders = data['Order ID'].nunique()
        total_quantity_item_sold = data['Quantity'].sum()
        customer_spending = data.groupby('Customer ID')['Total Price'].sum()
        top_customer = customer_spending.idxmax()
        top_customer_spending = customer_spending.max()
        avg_order_value = data['Total Price'].mean()

        print(f"Total Revune: {total_revune}\nTotal Numbers of Orders: {total_numbers_of_orders}\nTotal Quantity Item Sold: {total_quantity_item_sold}\nTop Customer: {top_customer}\nTop Customer Spending: {top_customer_spending}\nAvrage Order Value: {avg_order_value}")

if __name__ == "__main__":
    aeod = Analyzing_Ecommerce_Order_Data()
    aeod.data_summary()