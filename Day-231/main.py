import pandas
class car_showroom_management:
    def __init__(self):
        self.orders = []
        self.cars = []
        self.usr_info = []
    
    def usr_login(self):
        self.user_name = input("Enter your username: ")
        self.passwrd = input("Enter a password: ")
        self.usr_innfo = self.user_name, self.passwrd
        self.usr_info.append(self.usr_innfo)
    def main_menu(self):
        while True:
            admin_chs = int(input("1.Add Cars\n2.Add orders\n3.Dellete cars\n4.See Orders\n5.See Cars\n6.save the order data\n7.Exit\n: "))
            if admin_chs == 1:
                self.add_cars()
            elif admin_chs == 2:
                self.add_orders()
            elif admin_chs == 3:
                self.dellete_cars()
            elif admin_chs == 4:
                self.see_orders()
            elif admin_chs == 5:
                self.see_cars()
            elif admin_chs == 6:
                self.save_data()
            elif admin_chs == 7:
                print("Goodbye..")
                break

    def add_cars(self):
        self.car_name = input("Enter the car name: ")
        self.car_model = input("Enter the car model: ")
        self.car_brand = input("Enter the car brand: ")
        self.car_price = int(input("enter the car price: "))
        self.car_info = self.car_name, self.car_model, self.car_brand, self.car_price
        self.cars.append(self.car_info)
    def add_orders(self):
        self.cus_name = input("Enter the customer name: ")
        self.ord_car_brand = input("Enter which brand of car  they want: ")
        self.ord_car_model = input("Enter which model of car  they want: ")
        self.ord_id = input("Add order id: ")
    def dellete_cars(self):
        self.car_brand_for_dellete = input("Enter the car brand for delliting the car: ")
        if self.car_brand_for_dellete in self.car_brand:
            self.cars.remove(self.car_brand_for_dellete)
        else:
            print("Something went wrong")
    def see_orders(self):
        print(f"The orders:\n{self.orders}")
    def see_cars(self):
        print(f"The cars:\n{self.cars}")
    def save_data(self):
        df = pandas.DataFrame(self.orders)
        file_name = f"{self.cus_name}_Orderinfo.txt"
        df.to_csv(file_name, index=False)
if __name__ == "__main__":
    manager = car_showroom_management()
    manager.usr_login()
    manager.main_menu()