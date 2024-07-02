import pandas as pd

def analyzie_sales_data():
    sales_data = {
        'Transaction ID	': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product D', 'Product B', 'Product A', 'Product E', 'Product D', 'Product C'],
        'Region': ['North','South','East','North','West','South','East','West','North','South'],
        'Sales Amount': [100, 150, 200, 120, 90, 130, 80, 110, 170, 160]
    }

    data = pd.DataFrame(sales_data)

    total_sales = data['Sales Amount'].sum()
    avrage_sales = data['Sales Amount'].mean()
    top_5_products = data.nlargest(5, 'Sales Amount')['Product']
    sales_by_region = data.groupby('Region')['Sales Amount'].sum()

    print(f"Total Sales: {total_sales}\nAvrage Sales: {avrage_sales}\nTop 5 Products: {top_5_products}\nSales By Region: {sales_by_region}")

analyzie_sales_data()