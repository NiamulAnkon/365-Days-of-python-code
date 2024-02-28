import datetime
import pandas
class Bakery_Management_System:
    def __init__(self):
        self.id = 0
        self.orders = []

    def main_menu(self):
        while True:
            usr_choice = int(input("1.Add Order\n2.View Order\n3.Save data to a TXT FILE\n4.Exit\nEnter your choice: "))

            if usr_choice == 1:
                self.add_orders()
            elif usr_choice == 2:
                self.view_order()
            elif usr_choice == 3:
                self.save_data()
            elif usr_choice == 4:
                print("Goodbye")
                break
            else:
                print("Something went wrong")
    
    def add_orders(self):
        self.cus_name = input("Enter the customer name: ")
        self.ord_quant = int(input("Enter the order quantitiy: "))
        self.ord_item = input("Enter the item name that user ordered: ")
        self.ord_id = int(input("Type a order id(in numbers only): "))
        self.cur_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ord_info = {'date': self.cur_date,'Customer Name': self.cus_name , 'Order Quantity': self.ord_quant , 'Item Name': self.ord_item , 'Order ID': self.ord_id }
        self.orders.append(self.ord_info)
        self.id += self.ord_id
    def view_order(self):
        print("Orders:")
        for orders in self.orders:
            print(orders)
    def save_data(self):
        df = pandas.DataFrame(self.orders)
        file_name = f"{self.cus_name}_order_info.txt"
        df.to_csv(file_name, index=False)
if __name__ == "__main__":
    bms = Bakery_Management_System()
    bms.main_menu()
