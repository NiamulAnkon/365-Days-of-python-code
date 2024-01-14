import time

print("-----Welcome to Gym-----")
time.sleep(9)

class Gym_membership_app:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age"))
        self.number = int(input("Enter your Number: "))
        self.email = input("Enter your email: ")
        self.info = self.name, self.age, self.email, self.number
        self.package()
        self.fix_date()
        self.usr_info_save_file()

    def package(self):
        print("Which Package you want:\n1.Beginer Package-500$ \n2.Intermediate Package-1,000$ \n3.Advance Package-1,500$ \n4.Ultra Package-2,000$")
        try:
            self.usr_choice = int(input("Enter which package you want: "))

            if self.usr_choice == 1:
                print("Alraight now pay 500$")
                pay = int(input("Enter the amount for pay: "))
                if pay ==500:
                    print( "Congrats Your Package is ready")
                elif pay > 500:
                    print( "The amount is too high")
                elif pay < 500:
                    print( "The amount is too low try again")
                else:
                    print( "Something went wrong")
            if self.usr_choice == 2:
                print("Alraight now pay 1,000$")
                pay = int(input("Enter the amount for pay: "))
                if pay == 1000:
                    print( "Congrats Your Package is ready")
                elif pay > 1000:
                    print( "The amount is too high")
                elif pay < 1000:
                    print( "The amount is too low try again")
                else:
                    print( "Something went wrong")
            if self.usr_choice == 3:
                print("Alraight now pay 500$")
                pay = int(input("Enter the amount for pay: "))
                if pay ==1500:
                    print( "Congrats Your Package is ready")
                elif pay > 1500:
                    print( "The amount is too high")
                elif pay < 1500:
                    print( "The amount is too low try again")
                else:
                    print( "Something went wrong")
            if self.usr_choice == 4:
                print("Alraight now pay 500$")
                pay = int(input("Enter the amount for pay: "))
                if pay ==2000:
                    print("Congrats Your Package is ready")
                elif pay > 2000:
                    print( "The amount is too high")
                elif pay < 2000:
                    print( "The amount is too low try again")
                else:
                    print( "Something went wrong")
        except ValueError:
            print("Something went wrong try again")

    def fix_date(self):
        self.usr_date = int(input("From When you want to join (day only): "))
        time.sleep(10)
        print(f"alraight your booking is set for: {self.usr_date}")
    
    def usr_info_save_file(self):
        usr_info = f"Coustomer  Info: {self.info}\nDate for start: {self.usr_date}\nselected package: {self.usr_choice}"
        file_name = f"{self.name}_information.txt"
        with open(file_name, "w") as file:
            file.write("".join(str(usr_info)))

if __name__ == "__main__":
    app = Gym_membership_app()