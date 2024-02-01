class Food_app_Management_System:
    def __init__(self):
        self.food_categories = ["appetizers", "main courses", "desserts"]

    def main_menu(self):
        while True:
            usr_chs = int(input("1.Buy Foods\n2.Select Category\n3.Exit\nEnter your choice: "))
            if usr_chs == 1:
                print("\n\n--------Type the name of the food you want to buy--------\n")
                usr_food_chs = input("Enter: ")
                print(f"The food you want to buy is {usr_food_chs}, and you have to pay 500$.")

                pay = int(input("Pay: "))
                if pay == 500:
                    print("Thanks for buying the food. Enjoy!")

                    usr_location = input("Enter your location: ")
                    print(f"Your order for {usr_food_chs} has been confirmed. It will be delivered to {usr_location}.")

            elif usr_chs == 2:
                self.show_categories()

            elif usr_chs == 3:
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

    def show_categories(self):
        print("\n--------Available Food Categories--------")
        for idx, category in enumerate(self.food_categories, 1):
            print(f"{idx}. {category}")
        cat_choice = int(input("Enter the category number: "))
        self.show_food_items(self.food_categories[cat_choice - 1])

    def show_food_items(self, category):
        print(f"\n--------{category.capitalize()}--------")
        print("Burger, Pizza, Shawrma e.t.c")
if __name__ == "__main__":
    app_foods = Food_app_Management_System()
    app_foods.main_menu()
