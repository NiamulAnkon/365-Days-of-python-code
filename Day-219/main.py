class Item_Exchanger_App:
    def __init__(self):
        self.items = []
        self.bal = 0
        self.accounts = []

    def create_account(self):
        self.username = input("Enter you username: ")
        self.password = input("Enter your password: ")
        self.acc_info = self.username, self.password
        self.accounts.append(self.acc_info)
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Add Item for Exchange\n2.Check Balance\n3.Check Items in Exchange List\n4.Exit\nEnter Your Choice: "))

            if usr_choice == 1:
                self.add_items()
            elif usr_choice == 2:
                self.check_bal()
            elif usr_choice == 3:
                self.check_items()
            elif usr_choice == 4:
                print("GoodBye :)")
                break
            else:
                print("Something went wrong Try again")
                continue
    def add_items(self):
        self.item_name = input("Enter the name of the item you want to put on exchange: ")
        self.item_des = input("Enter the item description: ")
        self.need_item = input("Enter the item you need for exchange: ")
        self.selling_price = int(input("Enter the selling Price: "))
        self.bal += self.selling_price
        self.item_info = self.item_name, self.item_des, self.need_item, self.selling_price
        self.items.append(self.item_info)
    def check_bal(self):
        print(f"Your balance{self.bal}")
    def check_items(self):
        print(f"You Items: {self.items}")
    
if __name__ == "__main__":
    apps = Item_Exchanger_App()
    apps.create_account()
    apps.main_menu()