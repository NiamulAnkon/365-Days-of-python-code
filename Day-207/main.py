import time
import random
class Text_based_Trading_Game:
    def __init__(self):
        self.money = 0
        self.items = ["Bitcoing", "doge coin", "T.V", "Computer", "Mobile"]
        self.inventory = []
        self.prices = 200000,100000,500,500000,20000
    def main_menu(self):
         while True:
            self.user_choice = int(input("1.Add Money\n2.Check Balance\n3.Check Inventory\n4.Buy Items\n5.Sell Items\n6.Exit\nEnter your choice: "))
            if self.user_choice == 1:
                self.Add_Money()
            elif self.user_choice == 2:
                 self.Check_Balance()
            elif self.user_choice == 3:
                 self.Check_Inventory()
            elif self.user_choice == 4:
                self.Buy_Items()
            elif self.user_choice == 5:
                 self.Sell_Items()
            elif self.user_choice == 6:
                 self.Exit()
    def Add_Money(self):
          self.money_amount = int(input("Enter the amount of money you want to add: "))
          self.money += self.money_amount
    def Check_Balance(self):
         print(f"Balance: {self.money}")
         time.sleep(5)
    def Check_Inventory(self):
         print(f"Inventory: {self.inventory}")
    def Buy_Items(self):
         print(f"Items: {self.items}")
         item_choice = input("Which item you want to buy : ")
         the_price = random.choice(self.prices)
         print(f"{item_choice} Price: {the_price}")
         pay_price = int(input("Pay: "))
         if pay_price == the_price:
                print(f"You have succesfully buy {item_choice}")
                self.inventory.append(item_choice)
         elif pay_price > the_price:
                print("The price is too high try again")
         elif pay_price < the_price:
                print("The amount is too low")
         else:
                print("Something try again")
    def Sell_Items(self):
         sell_item = input("Enter the name of the item you want to sell: ")
         sell_amount = int(input("Enter the amount of money for sell: "))
         print(f"You want to sell {sell_item}\nadn the amount of money you want to sell {sell_amount}")
         time.sleep(5)
         print("Congrats your item is sold now")
         self.money += sell_amount
    def Exit(self):
        print("Goodbye")
         
if __name__ == "__main__":
     game = Text_based_Trading_Game()
     game.main_menu()
         
