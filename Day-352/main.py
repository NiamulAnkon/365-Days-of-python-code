import pandas as pd

class inventory_managment_analysis:
    def data_analayzie(self):
        inventory_data = [
            {"Item ID": 1, "Item Name": "Item A", "Category": "Electronics", "Quantity": 50, "Unit Price": 300},
            {"Item ID": 2, "Item Name": "Item B", "Category": "Clothing", "Quantity": 100, "Unit Price": 50},
            {"Item ID": 3, "Item Name": "Item C", "Category": "Electronics", "Quantity": 30, "Unit Price": 200},
            {"Item ID": 4, "Item Name": "Item D", "Category": "Home Goods", "Quantity": 75, "Unit Price": 150},
            {"Item ID": 5, "Item Name": "Item E", "Category": "Clothing", "Quantity": 200, "Unit Price": 40},
            {"Item ID": 6, "Item Name": "Item F", "Category": "Home Goods", "Quantity": 60, "Unit Price": 100},
            {"Item ID": 7, "Item Name": "Item G", "Category": "Electronics", "Quantity": 20, "Unit Price": 400},
            {"Item ID": 8, "Item Name": "Item H", "Category": "Home Goods", "Quantity": 90, "Unit Price": 80},
            {"Item ID": 9, "Item Name": "Item I", "Category": "Clothing", "Quantity": 150, "Unit Price": 60},
            {"Item ID": 10, "Item Name": "Item J", "Category": "Electronics", "Quantity": 40, "Unit Price": 350}
        ]

        df = pd.DataFrame(inventory_data)

        total_stock =  df['Quantity'] * df['Unit Price']
        top_3_items_by_qunt = df.nlargest(3, 'Quantity')[['Item Name', 'Quantity']]
        stock_value_by_catageory = df.groupby('Category')['Unit Price'].sum()

        print(f"Total Stock: {total_stock}\nTop 3 Items By Quantity: {top_3_items_by_qunt}\nStock Value By Catageory: {stock_value_by_catageory}")

if __name__ == "__main__":
    ima = inventory_managment_analysis()
    ima.data_analayzie()    