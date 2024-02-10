class one_pay:
    def __init__(self):
        self.accounts = []
        self.balance = 0
    def create_account(self):
        self.first_name = input("Enter your First name: ")
        self.last_name = input("Enter your las name: ")
        self.nid_card_number = int(input("Enter your nid card number: "))
        self.date_of_birth = int(input("Enter your Birth of date: "))
        self.usr_info = self.first_name, self.last_name, self.nid_card_number, self.date_of_birth
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Add Money\n2.Withdraw Money\n3.Check Balance\n4.Exit"))
            if usr_choice == 1:
                self.add_money()
            elif usr_choice == 2:
                self.withdraw_money()
            elif usr_choice == 3:
                self.check_balance()
            elif usr_choice == 4:
                print("GoodBye")
                break
            else:
                print("Try Again")
            
    def add_money(self):
        self.amount = int(input("Enter the amount of money you want to add: "))
        self.balance += self.amount
    def withdraw_money(self):
        self.withdraw_amount = int(input("Enter the withdraw amount: "))
        if self.withdraw_amount > self.balance:
            print("Try again")
        else:
            print("Something went wrong")
        self.balance -= self.withdraw_amount
    def check_balance(self):
        print(f"{self.balance}")

    def usr_info(self):
        file_name = f"{self.first_name}.txt"
        usr_info = f"The user info: {self.usr_info}\nAccount balance: {self.balance}"
        with open(file_name, "w") as file:
            file.write("".join(usr_info))

if __name__ == "__main__":
    app = one_pay()
    app.create_account()
    app.main_menu()