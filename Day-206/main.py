import time
class Contact_Book_App:
    def __init__(self):
        self.contacts = []
        self.group = []
        self.group_members = []
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Add Contact\n2.View Contact\n3.Dellete Contact\n4.Create Group\n5.Add Members In Group\n6.Exit\nEnter your choice: "))
            if usr_choice == 1:
                self.add_contact()
            elif usr_choice == 2:
                self.view_contact()
            elif usr_choice == 3:
                self.dellete_contact()
            elif usr_choice == 4:
                self.create_group()
            elif usr_choice == 5:
                self.add_members_group()
            elif usr_choice == 6:
                print("GoodBye")
                break
            else:
                print("Something went wrong try again")
                continue
        
    def add_contact(self):
        self.usr_name = input("Enter the name: ")
        self.usr_phone_number = int(input("Enter the phone number: "))
        self.usr_email = input("Enter the email: ")
        self.usr_info = [self.usr_name, self.usr_phone_number, self.usr_email]
        self.contacts.append(self.usr_info)
    def view_contact(self):
        print(f"User Info:\n{self.usr_info}")
        time.sleep(5)
    def dellete_contact(self):
        usr_names = input("Enter the name you want to dellete: ")
        if usr_names in self.usr_name:
            self.contacts.remove(self.usr_info)
        else:
            print("Something went wrong")
    def create_group(self):
        self.group_name = input("Enter your group name: ")
        self.group.append(self.group_name)
    def add_members_group(self):
        self.add_members = input("Enter the name: ")
        if self.add_members == self.usr_name:
            self.group_members.append(self.add_members)
        else:
            print("Something went wrong")

if __name__ == "__main__":
    app = Contact_Book_App()
    app.main_menu()
