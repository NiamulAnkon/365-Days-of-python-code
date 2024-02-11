class Travel_Packing_Assistant:
    def __init__(self):
        self.trips = []
        self.packing_list = []
        self.catalog = []
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Plan Trips\n2.Check Trips\n3.Add Item Catalog\n4.Check Item Catalog\n5.Create Packing List\n6.Check Packing List\n7.Exit"))
            if usr_choice == 1:
                self.plan_trips()
            elif usr_choice == 2:
                self.check_trips()
            elif usr_choice == 3:
                self.add_item_catalog()
            elif usr_choice == 4:
                self.check_item_catalog()
            elif usr_choice == 5:
                self.create_item_catalog()
            elif usr_choice == 6:
                self.check_packing_list()
            elif usr_choice == 7:
                print("GoodBye :)")
                break
            else:
                print("Something went wrong")
                continue

    def plan_trips(self):
        self.destination = input("Enter your Destination: ")
        self.trip_catageory = input("Enter the trip catageory: ")
        self.how_day_long = int(input("Enter for how much day your trip will go: "))
        self.trip_info = self.destination, self.trip_catageory, self.how_day_long
        self.trips.append(self.trip_info)
    def check_trips(self):
        print(f"{self.trip_info}")
    def add_item_catalog(self):
        self.item_for_catalog = input("Enter the item that you want to add: ")
        self.catalog.append(self.item_for_catalog)
    def check_item_catalog(self):
        print(f"{self.catalog_info}")
    def create_item_catalog(self):
        self.catalog_name = input("Enter the name for catalog: ")
        self.catalog_items = input("Enter your items for catalog: ")
        self.catalog_info = self.item_for_catalog
        self.catalog.append(self.catalog_info)
    def check_packing_list(self):
        print(f"{self.packing_list}")



if __name__ == "__main__":
    apps = Travel_Packing_Assistant()
    apps.main_menu()