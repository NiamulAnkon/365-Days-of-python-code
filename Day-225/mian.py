class Event_ticket_buy:
    def __init__(self):
        self.evets = ["Sports", "Concert"]
        self.tickets = 100
        self.brought_ticket = 0
        
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Buy Ticket,\n2.see Tickets you have brought\n3.See avalable tickets\n4.see events\n5.Exit\nenter your Choice:  "))
            if usr_choice == 1:
                self.buy_ticket()
            elif usr_choice == 2:
                self.brought_tickets()
            elif usr_choice == 3:
                self.avalibale_tickets()
            elif usr_choice == 4:
                self.see_events()
            elif usr_choice == 5:
                print("GoodBye :)")
                break
            else:
                print("Somethig went wrong try again")
                continue
    
    def buy_ticket(self):
        self.tik_eve_name = input("For Which event ticket you want to buy: ")
        print("Ticket price: 50$")
        self.pay = int(input("pay: "))
        if self.pay == 50:
            self.tickets -= 1
            self.brought_ticket += 1
            print("Congrats you have correctly brought ticket")
        else:
            print("Something went wrong")
    def brought_tickets(self):
        print(f"Your Brought Tickets are: {self.brought_ticket}")
    def avalibale_tickets(self):
        print(f"{self.tickets} Tickets are avalabel")
    def see_events(self):
        print(f"The Events that are avilable is: {self.evets}")
    
if __name__ == "__main__":
    app = Event_ticket_buy()
    app.main_menu()