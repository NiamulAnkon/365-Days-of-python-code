class Event_Management_System:
    def __init__(self):
        self.users = []
        self.events = []

    def register(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.password = input("Chose a password: ")
        self.usr_info = self.name, self.email, self.password
        self.users.append(self.usr_info)
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Create Event\n2.See Events\n3.Exit"))
            
            if usr_choice == 1:
                self.create_event()
            elif usr_choice == 2:
                self.see_events()
            elif usr_choice == 3:
                print("GoodBye :)")
                break
            else:
                print("Try again")
                continue
        
    def create_event(self):
        self.event_name = input("Enter your event name: ")
        self.event_date = int(input("Enter your event date: "))
        self.event_place = input("Where this event will be organize: ")
        self.event_invinted_people = input("Enter who you want to invite: ")
        self.event_info = [self.event_name, self.event_date, self.event_place, self.event_invinted_people]
    def see_events(self):
        print(f"The event info: {self.event_info}")


if __name__ == "__main__":
    app = Event_Management_System()
    app.register()
    app.main_menu()
