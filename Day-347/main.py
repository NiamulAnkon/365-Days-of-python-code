import pandas as pd

def Customer_Orders_Analysis():
    orders_data = {
        'Order ID': [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10],
        'Customer ID': ['C001', 'C002', 'C001', 'C003', 'C002', 'C004', 'C001', 'C003', 'C002', 'C004'],
        'Order Date': ['2023-01-15', '2023-02-20', '2023-03-25', '2023-04-10', '2023-06-20', '2023-05-15', '2023-07-05', '2023-08-15', '2023-09-20', '2023-10-25'],
        'Order Amount': [250, 300, 200, 450, 100, 500, 350, 400, 250, 100],
    }

    df = pd.DataFrame(orders_data)

    total_number_of_orders = df['Order ID'].count()
    avrage_order_value = df['Order Amount'].mean()
    top_3_customers = df.nlargest(3, 'Order Amount')['Customer ID']
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%Y-%m-%d')
    df['Month'] = df['Order Date'].dt.to_period('M')
    orders_by_month = df.groupby('Month')['Order ID'].count()
    print(f"Total Numbers of Orders: {total_number_of_orders}\n\nAvrage Order Value: {avrage_order_value:.2f}\n\nTop 3 Customers by order value\n: {top_3_customers.to_string(index=False)}\nOrders By Month: {orders_by_month}")

if __name__ == "__main__":
    Customer_Orders_Analysis()