import pandas
class grocrey_sotre_management_system:
    def __init__(self):
        self.orders = []
        self.items = {
            'Apple': 2,
            'Beef': 30,
            'chicken': 20,
            'butter': 10,
            'egg': 20
        }
    
    def main_menu(self):
        while True:
            admin_chs = int(input("1.Add Orders\n2.Watch items\n3.See Orders\n4.Save order data\n5.Save items data\n6.Exit\n: "))
            if admin_chs == 1:
                self.add_orders()
            elif admin_chs == 2:
                self.watch_items()
            elif admin_chs == 3:
                self.see_orders()
            elif admin_chs == 4:
                self.save_ord_data()
            elif admin_chs == 5:
                self.save_item_data()
            elif admin_chs == 6:
                print("Exiting")
                break

    
    def add_orders(self):
        self.cus_name = input("ENter the customer name: ")
        self.item_name = input("Enter the item that customer ordered: ")
        self.item_quant = int(input("Enter the quantity: "))
        self.ord_info = self.cus_name, self.item_name, self.item_quant
        self.orders.append(self.ord_info)
    def watch_items(self):
        print(f"Items:\n{self.items}")
    def see_orders(self):
        print(f"Orders:\n{self.orders}")
    def save_ord_data(self):
        df_ord_data = pandas.DataFrame(self.orders)
        file_name = f"{self.cus_name}_ord_info.txt"
        df_ord_data.to_csv(file_name, index=False)
    def save_item_data(self):
        df_item_data = pandas.DataFrame(list(self.items.items()), columns=['Item', 'Quantity'])
        file_name = "Items_data.txt"
        df_item_data.to_csv(file_name, index=False)
        print(f"Items data saved to {file_name}")


if __name__ == "__main__":
    gms = grocrey_sotre_management_system()
    gms.main_menu()