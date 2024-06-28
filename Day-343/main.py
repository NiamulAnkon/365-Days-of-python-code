import pandas as pd
class Analyzing_Retail_Store_Inventory_Data:
    def Data_sumarry(self):
        data = {
            'Product ID': [1, 2, 3, 4, 5, 6, 7, 8],
            'Product Name': ['Shampoo', 'Toothpaste', 'Apples', 'Bread', 'Detergent', 'Milk', 'Soap', 'Chicken'],
            'Category': ['Personal Care', 'Personal Care', 'Groceries', 'Groceries', 'Household', 'Groceries', 'Personal Care', 'Groceries'],
            'Stock Quantity': [50, 30, 100, 20, 40, 60, 70, 25],
            'Reorder Level': [20, 10, 30, 10, 15, 20, 25, 10],
            'Price per Unit': [5.99, 2.99, 0.99, 1.99, 7.99, 2.49, 1.49, 5.49]
        }
        df = pd.DataFrame(data)

        total_stock_quantity = df['Stock Quantity'].sum()
        total_inventory_value = df['Total Value'].sum()
        category_stock_quantity = df.groupby('Category')['Stock Quantity'].sum()
        category_inventory_value = df.groupby('Category')['Total Value'].sum()
        reorder_products = df[df['Stock Quantity'] <= df['Reorder Level']]
        total_reorder_products = reorder_products.shape[0]
        most_expensive_product = df.loc[df['Price per Unit'].idxmax()]['Product Name']
        least_expensive_product = df.loc[df['Price per Unit'].idxmin()]['Product Name']

        print(f"Total Stock Quantity: {total_stock_quantity}\nTotal Inventory Value: {total_inventory_value}\nCategory_stock Quantity: {category_stock_quantity}\nCategory Inventiry Value: {category_inventory_value}\nTotal Reorder Products: {total_reorder_products}\nMost Expensive Product: {most_expensive_product}\nLeast Expensive Product: {least_expensive_product}")

if __name__ == "__main__":
    arsid = Analyzing_Retail_Store_Inventory_Data()
    arsid.Data_sumarry()