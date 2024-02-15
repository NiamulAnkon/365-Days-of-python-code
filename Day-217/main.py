class Shpong_List_Manager:
    def __init__(self):
        self.shping_list = []
        
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Add Items on Shoping list\n2Dellete Items On Shoping list\n3.Check The Shoping List\n4.Exit\nEnter your choice: "))
            if usr_choice == 1:
                self.add_items_on_shoping()
            elif usr_choice == 2:
                self.Dellete_items()
            elif usr_choice == 3:
                self.show_list()
            elif usr_choice == 4:
                print("GoodBye :)")
                break
            else:
                print("Something Went Wrong")
                continue
    def add_items_on_shoping(self):
        self.item_name = input("Enter the name of the item you want to add on your shoping list: ")
        self.item_catageory = input("Enter the catageory: ")
        self.item_price = int(input("Enter the item price: "))
        self.item_info  = self.item_name, self.item_catageory, self.item_price
        self.shping_list.append(self.item_info)
    def Dellete_items(self):
        self.item_name_for_dellete = input("Enter your item name of delleting: ")
        if self.item_name_for_dellete in self.item_name:
            self.shping_list.remove(self.item_name_for_dellete)
        else:
            print("Try Again")
    def show_list(self):
        print(f"The Shoping List\n{self.item_info}")



if __name__ == "__main__":
    List_app = Shpong_List_Manager()
    List_app.main_menu()
